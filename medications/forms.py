from django import forms
from .models import Medication
from django.utils.html import format_html

class MedicationForm(forms.ModelForm):
    name = forms.ChoiceField(
        choices=Medication.MEDICATION_CHOICES,  # Use the grouped choices directly
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'medication-select'
        })
    )
    
    frequency = forms.ChoiceField(
        choices=Medication.FREQUENCY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'frequency-select'
        })
    )
    
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
    )

    active = forms.BooleanField(
        required=False,  # This allows the field to be unchecked
        initial=True,    # Sets default value to checked
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500',  # Tailwind classes for checkbox
        })
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any additional notes about this medication'
        })
    )

    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'notes']