from django.urls import path

from . import views

url_patterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
] 
