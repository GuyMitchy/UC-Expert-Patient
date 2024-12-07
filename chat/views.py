from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .models import Conversation, Message
from knowledge.manager import with_rag
from django.contrib import messages


class ConversationListView(LoginRequiredMixin, ListView):
    model = Conversation
    template_name = 'chat/list.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)


class ConversationCreateView(LoginRequiredMixin, CreateView):
    model = Conversation
    template_name = 'chat/new_conversation.html'
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('chat:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Set the user before saving
        form.instance.user = self.request.user
        response = super().form_valid(form)

        # Create welcome message
        Message.objects.create(
            conversation=self.object,
            content="Hello! I'm your UC Expert assistant."
            "I can help answer questions about Ulcerative Colitis, "
            "your symptoms, and medications. What would you like to know?",
            is_bot=True
        )

        return response


class ConversationDetailView(LoginRequiredMixin, DetailView):
    model = Conversation
    template_name = 'chat/detail.html'
    context_object_name = 'conversation'

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = self.object.message_set.all()
        return context


class ConversationDeleteView(LoginRequiredMixin, DeleteView):
    model = Conversation
    template_name = 'chat/delete.html'
    success_url = reverse_lazy('chat:list')

    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Conversation deleted successfully.')
        return super().delete(request, *args, **kwargs)


@login_required
@with_rag
def send_message(request, conversation_id, rag=None):
    """Handle message sending with managed RAG instance"""
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=405)

    try:
        conversation = get_object_or_404(
            Conversation, id=conversation_id, user=request.user
            )
        user_message = request.POST.get('message', '').strip()

        if not user_message:
            return HttpResponse('Message is required', status=400)

        # Save user message
        user_message_obj = Message.objects.create(
            conversation=conversation,
            content=user_message,
            is_bot=False
        )

        # Build user context
        user_context = "User Context:\n"

        # Add Conversation History - last 10 messages
        previous_messages = conversation.message_set.order_by(
            '-created_at'
            )[:10][::-1]
        conversation_history = "\nConversation History:\n"
        for msg in previous_messages:
            role = "User" if not msg.is_bot else "Assistant"
            conversation_history += f"{role}: {msg.content}\n"

        # Get symptoms
        try:
            recent_symptoms = request.user.symptom_set.all()
            if recent_symptoms:
                user_context += "\nRecent Symptoms:\n"
                for symptom in recent_symptoms:
                    symptom_date = symptom.date.strftime('%Y-%m-%d')
                    user_context += (
                        f"- {symptom.type} on {symptom_date}: "
                        f"{symptom.description} "
                        f"(Severity: {symptom.severity})\n"
                    )
        except AttributeError:
            user_context += "\nNo symptoms recorded.\n"

            # Get medications
        try:
            active_medications = request.user.medication_set.filter(
                active=True
                )
            if active_medications:
                user_context += "\nCurrent Medications:\n"
                for med in active_medications:
                    med_date = med.start_date.strftime('%Y-%m-%d')
                    user_context += (
                        f"- Started {med_date}: {med.get_name_display()} "
                        f"({med.dosage}, {med.get_frequency_display()}, "
                        f"{med.notes})\n"
                    )
        except AttributeError:
            user_context += "\nNo medications recorded.\n"

# Try to get food entries if they exist
        try:
            recent_foods = request.user.food_set.all()
            if recent_foods:
                user_context += "\nRecent Food Entries:\n"
                for food in recent_foods:
                    food_date = food.eaten_at.strftime('%Y-%m-%d %H:%M')
                    user_context += (
                        f"- Food diary entry:{food_date}: "
                        f"{food.get_meal_type_display()} - {food.food_name} "
                        f"({food.portion_size}) is_trigger:{food.is_trigger}"
                    )
                    if food.notes:
                        user_context += f" Notes: {food.notes}"
                    user_context += "\n"
        except AttributeError:
            user_context += "\nNo food entries recorded.\n"

        # Get response using managed RAG instance
        response = rag.get_response(
            question=user_message,
            user_info=user_context,
            conversation_history=conversation_history
        )

        # Save bot message and render response
        bot_message = Message.objects.create(
            conversation=conversation,
            content=response,
            is_bot=True
        )

        messages_html = render_to_string(
            'chat/message.html', {'message': user_message_obj}
            )
        messages_html += render_to_string(
            'chat/message.html', {'message': bot_message}
            )

        return HttpResponse(messages_html)

    except Exception as e:
        print(f"Error in send_message: {str(e)}")
        return HttpResponse(f"Error: {str(e)}", status=500)
