from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from .models import Food
from django.utils.html import format_html

class FoodForm(forms.ModelForm):
    food_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter food'
        })
    )
    
    meal_type = forms.ChoiceField(
        choices=Food.MEAL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'meal-select'
        })
    )
    
    eaten_at = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    portion_size = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter portion size (e.g., small, med, large)'
        })
    )
    
    is_trigger = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500'
        })
    )

    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any additional notes about this meal'
        })
    )

    class Meta:
        model = Food
        fields = ['food_name', 'meal_type', 'eaten_at', 'portion_size']
        widgets = {
            'description': SummernoteWidget(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'space-y-4'
        
        if self.instance.pk and self.instance.eaten_at:
            self.initial['eaten_at'] = self.instance.eaten_at.strftime('%Y-%m-%dT%H:%M')