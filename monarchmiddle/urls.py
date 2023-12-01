# monarchmiddle/urls.py
from django.urls import path
from .views import password_protect

urlpatterns = [
    path('password_protect/', password_protect, name='password_protect'),
]
