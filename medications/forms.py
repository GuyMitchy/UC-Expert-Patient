from django import forms
from .models import Medication
from django.utils import timezone


class MedicationForm(forms.ModelForm):
    # Base class for consistent styling
    BASE_INPUT_CLASS = (
        "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
        "focus:border-blue-500 focus:ring-blue-500"
    )

    name = forms.ChoiceField(
        choices=Medication.MEDICATION_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_INPUT_CLASS,
            'id': 'medication-select'
        })
    )

    frequency = forms.ChoiceField(
        choices=Medication.FREQUENCY_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_INPUT_CLASS,
            'id': 'frequency-select'
        })
    )

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': BASE_INPUT_CLASS,
            'max': timezone.now().strftime('%Y-%m-%d')
        })
    )

    dosage = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': BASE_INPUT_CLASS,
            'placeholder': 'Enter dosage (e.g., 40mg)'
        })
    )

    active = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'class': (
                'h-4 w-4 rounded border-gray-300'
                'text-blue-600 focus:ring-blue-500'
                )
        })
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': BASE_INPUT_CLASS,
            'rows': 3,
            'placeholder': 'Any additional notes about this medication'
        })
    )

    class Meta:
        model = Medication
        fields = [
            'name', 'dosage', 'frequency', 'start_date', 'active', 'notes'
            ]
