from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Реєструє нового користувача"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Виконуємо вхід та перенаправляємо користувача на домашню сторінку
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)
