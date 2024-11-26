# forms.py
from django import forms
from .models import Symptom
from django.utils import timezone

class SymptomForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'max': timezone.now().strftime('%Y-%m-%d')  # Todays date
        })
    )
    
    type = forms.ChoiceField(
        choices=Symptom.SYMPTOM_TYPES,
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'id': 'symptom-type-select'
        })
    )
    
    severity = forms.ChoiceField(
        choices=Symptom.SEVERITY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'id': 'severity-select'
        })
    )
    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'rows': 3,
            'placeholder': 'Describe your symptoms (optional)'
        })
    )

    class Meta:
        model = Symptom
        fields = ['date', 'type', 'severity', 'description']