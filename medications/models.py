from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date


def validate_past_date(value):
    if value > date.today():
        raise ValidationError('Date cannot be in the future.')


class Medication(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('twice_daily', 'Twice Daily'),
        ('three_times_daily', 'Three Times Daily'),
        ('four_times_daily', 'Four Times Daily'),
        ('weekly', 'Weekly'),
        ('every_other_week', 'Every Other Week'),
        ('monthly', 'Monthly'),
        ('as_needed', 'As Needed'),
    ]

    MEDICATION_CHOICES = [
        ('5-ASAs', (
            ('MESALAZINE_ORAL', 'Mesalazine (Oral)'),
            ('MESALAZINE_TOPICAL', 'Mesalazine (Topical)'),
            ('SULFASALAZINE', 'Sulfasalazine'),
            ('BALSALAZIDE', 'Balsalazide'),
            ('OLSALAZINE', 'Olsalazine'),
        )),
        ('Corticosteroids', (
            ('PREDNISOLONE', 'Prednisolone'),
            ('BUDESONIDE', 'Budesonide'),
            ('HYDROCORTISONE', 'Hydrocortisone'),
            ('BECLOMETHASONE', 'Beclomethasone'),
        )),
        ('Immunomodulators', (
            ('AZATHIOPRINE', 'Azathioprine'),
            ('MERCAPTOPURINE', 'Mercaptopurine'),
            ('METHOTREXATE', 'Methotrexate'),
            ('CYCLOSPORINE', 'Cyclosporine'),
            ('TACROLIMUS', 'Tacrolimus'),
        )),
        ('Biologics', (
            ('INFLIXIMAB', 'Infliximab'),
            ('ADALIMUMAB', 'Adalimumab'),
            ('GOLIMUMAB', 'Golimumab'),
            ('VEDOLIZUMAB', 'Vedolizumab'),
            ('USTEKINUMAB', 'Ustekinumab'),
            ('RISANKIZUMAB', 'Risankizumab'),
        )),
        ('JAK Inhibitors', (
            ('TOFACITINIB', 'Tofacitinib'),
            ('UPADACITINIB', 'Upadacitinib'),
        ))
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50, choices=MEDICATION_CHOICES)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    start_date = models.DateField(validators=[validate_past_date])
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_name_display()} - {self.dosage}"

    class Meta:
        ordering = ['-active', '-start_date']
