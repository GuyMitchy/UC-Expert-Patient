from django.contrib import admin
from .models import Symptom


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'severity', 'date')
    list_filter = ('type', 'severity', 'date')
    search_fields = ('user__username', 'description')
    date_hierarchy = 'date'
