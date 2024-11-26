from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import date
from .models import Food
from .forms import FoodForm
from django.utils import timezone

class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = 'food/list.html'
    context_object_name = 'foods'
    
    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)

class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/add.html'
    success_url = reverse_lazy('food:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Meal added successfully.')
        return super().form_valid(form)

class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/edit.html'
    success_url = reverse_lazy('food:list')

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Meal updated successfully.')
        return super().form_valid(form)

class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = 'food/delete.html'
    success_url = reverse_lazy('food:list')

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Meal deleted successfully.')
        return super().delete(request, *args, **kwargs)