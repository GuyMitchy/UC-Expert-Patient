from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

def validate_past_date(value): # This gets used in the model as (validators=validate_past_date)
    if value > date.today():
        raise ValidationError('Date cannot be in the future.')

class Symptom(models.Model):
    SEVERITY_CHOICES = [
        (1, 'Very Mild'),
        (2, 'Mild'),
        (3, 'Moderate'),
        (4, 'Severe'),
        (5, 'Very Severe'),
    ]

    SYMPTOM_TYPES = [
        ('pain', 'Abdominal Pain'),
        ('blood', 'Blood in Stool'),
        ('urgency', 'Urgency'),
        ('fatigue', 'Fatigue'),
        ('joint_pain', 'Joint Pain'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(validators=[validate_past_date], default=date.today)
    type = models.CharField(max_length=100, choices=SYMPTOM_TYPES, default='other')
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_type_display()} - {self.get_severity_display()} ({self.date})"
