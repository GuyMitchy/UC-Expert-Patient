from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Food
from .forms import FoodForm
from django.utils import timezone


class FoodListView(LoginRequiredMixin, ListView):
    """
    View for displaying a list of food entries for the logged-in user.
    
    Inherits from:
        LoginRequiredMixin: Ensures user authentication
        ListView: Handles listing of Food objects
    
    Attributes:
        model: Food model
        template_name: Path to the list template
        context_object_name: Name used for the food list in template context
    """
    model = Food
    template_name = 'foods/list.html'
    context_object_name = 'foods'

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)


class FoodCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating new food entries.
    
    Inherits from:
        LoginRequiredMixin: Ensures user authentication
        CreateView: Handles creation of Food objects
    
    Attributes:
        model: Food model
        form_class: Form class for food creation
        template_name: Path to the creation template
        success_url: URL to redirect to after successful creation
    """
    model = Food
    form_class = FoodForm
    template_name = 'foods/add.html'
    success_url = reverse_lazy('foods:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Meal added successfully.')
        return super().form_valid(form)


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating existing food entries.
    
    Inherits from:
        LoginRequiredMixin: Ensures user authentication
        UpdateView: Handles updating of Food objects
    
    Attributes:
        model: Food model
        form_class: Form class for food updating
        template_name: Path to the edit template
        success_url: URL to redirect to after successful update
    """
    model = Food
    form_class = FoodForm
    template_name = 'foods/edit.html'
    success_url = reverse_lazy('foods:list')

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Meal updated successfully.')
        return super().form_valid(form)


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting food entries.
    
    Inherits from:
        LoginRequiredMixin: Ensures user authentication
        DeleteView: Handles deletion of Food objects
    
    Attributes:
        model: Food model
        template_name: Path to the deletion confirmation template
        success_url: URL to redirect to after successful deletion
    """
    model = Food
    template_name = 'foods/delete.html'
    success_url = reverse_lazy('foods:list')

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Meal deleted successfully.')
        return super().delete(request, *args, **kwargs)
