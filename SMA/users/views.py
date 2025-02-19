# users/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully!')
            return redirect('global_feed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('global_feed')