from django.contrib import admin
from .models import Medication

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dosage', 'active', 'start_date')
    list_filter = ('active', 'name', 'start_date')
    search_fields = ('user__username', 'notes')
    date_hierarchy = 'start_date'