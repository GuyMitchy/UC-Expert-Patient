"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [   
    path('admin/', admin.site.urls), 
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('symptoms/', include('symptoms.urls')),
    path('medications/', include('medications.urls')),
    path('foods/', include('foods.urls')),
    path('chat/', include('chat.urls')),
    path('privacy/', TemplateView.as_view(template_name='pages/privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
    path('disclaimer/', TemplateView.as_view(template_name='pages/disclaimer.html'), name='disclaimer'),
    path('data-protection/', TemplateView.as_view(template_name='pages/data_protection.html'), name='data-protection'),
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('guide/', TemplateView.as_view(template_name='pages/guide.html'), name='guide'),
]
