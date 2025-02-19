# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
        extra_context={'messages': {'success': 'Welcome back! You are now logged in.'}}), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
