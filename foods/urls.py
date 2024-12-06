from django.urls import path
from . import views


app_name = 'foods'

urlpatterns = [
    path('', views.FoodListView.as_view(), name='list'),
    path('add/', views.FoodCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.FoodUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.FoodDeleteView.as_view(), name='delete'),
]
