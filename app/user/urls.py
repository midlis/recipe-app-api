"""
URL mappings for the user API.
"""

from django.urls import path
from user import views

APP_NAME = 'user'

urlpatterns = [path('create/', views.CreateUserView.as_view(), name='create')]
