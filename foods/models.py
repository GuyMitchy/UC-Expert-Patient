from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError


def validate_past_date(value):
    # Convert value to datetime for comparison if needed
    if isinstance(value, date):
        today = timezone.now().date()
        if value > today:
            raise ValidationError('Date cannot be in the future.')


class Food(models.Model):

    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    DISCOMFORT_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    IS_TRIGGER_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unsure', 'Unsure'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    date = models.DateField(validators=[validate_past_date])
    eaten_at = models.TimeField(default=timezone.now)
    meal_type = models.CharField(max_length=50, choices=MEAL_CHOICES)
    food_name = models.CharField(max_length=50)
    portion_size = models.CharField(max_length=50)
    discomfort = models.CharField(max_length=50, choices=DISCOMFORT_CHOICES)
    is_trigger = models.CharField(max_length=50, choices=IS_TRIGGER_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal_type} - {self.food_name}"

    class Meta:
        ordering = ['-date', '-eaten_at']
