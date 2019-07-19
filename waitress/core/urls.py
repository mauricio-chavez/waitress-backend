"""Core app urls"""

from django.urls import path
from django.http import JsonResponse

def index(request):
    """Example page"""
    return JsonResponse({
        "message": "Yes, I'm working, bitch"
    })

urlpatterns = [
    path('', index, name='index'),
]