# forms.py
from django import forms
from .models import Symptom
from django.utils import timezone


class SymptomForm(forms.ModelForm):
    BASE_CLASS = (
        "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
        "focus:border-blue-500 focus:ring-blue-500"
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': BASE_CLASS,
            'max': timezone.now().strftime('%Y-%m-%d')  # Today's date
        })
    )

    type = forms.ChoiceField(
        choices=Symptom.SYMPTOM_TYPES,
        widget=forms.Select(attrs={
            'class': BASE_CLASS,
            'id': 'symptom-type-select'
        })
    )

    severity = forms.ChoiceField(
        choices=Symptom.SEVERITY_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_CLASS,
            'id': 'severity-select'
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': BASE_CLASS,
            'rows': 3,
            'placeholder': 'Describe your symptoms (optional)'
        })
    )

    class Meta:
        model = Symptom
        fields = ['date', 'type', 'severity', 'description']
