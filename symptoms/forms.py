from django import forms
from crispy_forms.helper import FormHelper
from .models import Symptom

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['date', 'severity', 'description', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'space-y-4'