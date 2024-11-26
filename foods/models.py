from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date

# Create your models here.

def validate_past_date(value): # This gets used in the model as (validators=validate_past_date)
    if value > timezone.now():
        raise ValidationError('Date cannot be in the future.')

class Food(models.Model):
    
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),  
        ('snack', 'Snack'),    
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(validators=[validate_past_date], default=timezone.now)
    eaten_at = models.TimeField(default=timezone.now)
    meal_type = models.CharField(max_length=50, choices=MEAL_CHOICES)
    food_name = models.CharField(max_length=50)
    portion_size = models.CharField(max_length=50)
    is_trigger = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.meal_type} - {self.food_name}"

    class Meta:
        ordering = ['-date','-eaten_at',]