from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.ConversationListView.as_view(),
        name='list'),
    path('new/', views.ConversationCreateView.as_view(),
        name='new'),
    path('<int:pk>/', views.ConversationDetailView.as_view(),
        name='detail'),
    path('<int:pk>/delete', views.ConversationDeleteView.as_view(),
        name='delete'),
    path('<int:conversation_id>/send/', views.send_message,
        name='send_message'),
]
