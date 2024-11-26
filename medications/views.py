from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import date
from .models import Medication
from .forms import MedicationForm

class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
    template_name = 'medications/list.html'
    context_object_name = 'medications'
    
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

class MedicationCreateView(LoginRequiredMixin, CreateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'medications/add.html'
    success_url = reverse_lazy('medications:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Medication added successfully.')
        return super().form_valid(form)

class MedicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Medication
    form_class = MedicationForm
    template_name = 'medications/edit.html'
    success_url = reverse_lazy('medications:list')

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Medication updated successfully.')
        return super().form_valid(form)

class MedicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Medication
    template_name = 'medications/delete.html'
    success_url = reverse_lazy('medications:list')

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Medication deleted successfully.')
        return super().delete(request, *args, **kwargs)
