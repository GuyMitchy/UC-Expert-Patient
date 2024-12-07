from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from .models import Food
from django.utils import timezone


class FoodForm(forms.ModelForm):
    BASE_CLASS = (
        "mt-1 block w-full rounded-md border-gray-300 shadow-sm "
        "focus:border-blue-500 focus:ring-blue-500"
    )

    food_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': BASE_CLASS,
            'placeholder': 'Enter food'
        })
    )

    meal_type = forms.ChoiceField(
        choices=Food.MEAL_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_CLASS,
            'id': 'meal-select'
        })
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': BASE_CLASS,
            'max': timezone.now().strftime('%Y-%m-%d')
        })
    )

    eaten_at = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': BASE_CLASS,
        })
    )

    portion_size = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': BASE_CLASS,
            'placeholder': 'Enter portion size (e.g., small, med, large)'
        })
    )

    discomfort = forms.ChoiceField(
        choices=Food.DISCOMFORT_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_CLASS
        })
    )

    is_trigger = forms.ChoiceField(
        choices=Food.IS_TRIGGER_CHOICES,
        widget=forms.Select(attrs={
            'class': BASE_CLASS
        })
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': BASE_CLASS,
            'rows': 3,
            'placeholder': 'Any additional notes about this meal'
        })
    )

    class Meta:
        model = Food
        fields = [
            'food_name', 'meal_type', 'date', 'eaten_at',
            'portion_size', 'discomfort', 'is_trigger', 'notes'
        ]
        widgets = {
            'description': SummernoteWidget(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'space-y-4'

        if self.instance.pk and self.instance.eaten_at:
            self.initial['eaten_at'] = (
                self.instance.eaten_at.strftime('%H:%M')
            )
