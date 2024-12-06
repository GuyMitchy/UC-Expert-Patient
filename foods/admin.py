from django.contrib import admin
from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_name', 'meal_type', 'date', 'is_trigger')
    list_filter = ('meal_type', 'is_trigger', 'date')
    search_fields = ('user__username', 'food_name', 'notes')
    date_hierarchy = 'date'
