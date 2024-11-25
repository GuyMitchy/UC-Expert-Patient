from django.urls import path
from . import views

app_name = 'symptoms'

urlpatterns = [
    path('', views.SymptomListView.as_view(), name='list'),
    path('add/', views.SymptomCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.SymptomUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.SymptomDeleteView.as_view(), name='delete'),
] 