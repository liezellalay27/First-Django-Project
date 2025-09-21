# TrickIt/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task-list'),
    path('update/<int:pk>/', views.update_task, name='update-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('register/', views.register, name='register'),
]