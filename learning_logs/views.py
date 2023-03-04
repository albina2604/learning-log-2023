from django.shortcuts import render

# Create your views here.


def index(request):
    """Головна сторінка додатку Learning Log"""
    return render(request, 'learning_logs/index.html')
