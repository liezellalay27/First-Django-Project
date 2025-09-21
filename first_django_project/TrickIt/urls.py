# TrickIt/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task-list'),
    path('register/', views.register, name='register'),
    path('tasks/update/<int:pk>/', views.update_task, name='update-task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete-task'),
]