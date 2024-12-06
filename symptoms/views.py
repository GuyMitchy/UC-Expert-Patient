from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import date
from .models import Symptom
from .forms import SymptomForm


class SymptomListView(LoginRequiredMixin, ListView):
    model = Symptom
    template_name = 'symptoms/list.html'
    context_object_name = 'symptoms'

    def get_queryset(self):
        return Symptom.objects.filter(user=self.request.user)


class SymptomCreateView(LoginRequiredMixin, CreateView):
    model = Symptom
    form_class = SymptomForm
    template_name = 'symptoms/add.html'

    success_url = reverse_lazy('symptoms:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Symptom added successfully.')
        return super().form_valid(form)


class SymptomUpdateView(LoginRequiredMixin, UpdateView):
    model = Symptom
    form_class = SymptomForm
    template_name = 'symptoms/edit.html'

    success_url = reverse_lazy('symptoms:list')

    def get_queryset(self):
        # Ensure users can only edit their own symptoms
        return Symptom.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Symptom updated successfully.')
        return super().form_valid(form)


class SymptomDeleteView(LoginRequiredMixin, DeleteView):
    model = Symptom
    template_name = 'symptoms/delete.html'
    success_url = reverse_lazy('symptoms:list')

    def get_queryset(self):
        # Ensure users can only delete their own symptoms
        return Symptom.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Symptom deleted successfully.')
        return super().delete(request, *args, **kwargs)
