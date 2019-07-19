"""Core app urls"""

from django.urls import path


def index(request):
    """Example page"""
    from django.shortcuts import render
    return render(request, 'index.html')


urlpatterns = [
    path('', index, name='index'),
]
