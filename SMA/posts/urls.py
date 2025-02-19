# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.global_feed, name='global_feed'),
    path('profile/', views.user_profile, name='user_profile'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Add this line
]
