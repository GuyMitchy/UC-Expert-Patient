from django.urls import path
from . import views


app_name = 'medications'

urlpatterns = [
    path(
        '', views.MedicationListView.as_view(), name='list'
        ),
    path(
        'add/', views.MedicationCreateView.as_view(), name='add'
        ),
    path(
        '<int:pk>/edit/', views.MedicationUpdateView.as_view(), name='edit'
        ),
    path(
        '<int:pk>/delete/', views.MedicationDeleteView.as_view(), name='delete'
        ),
]
