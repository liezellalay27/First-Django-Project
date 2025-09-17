from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Make sure you import the Task model
from .models import Task 

def home(request):
    return render(request, 'home.html')

@login_required
def task_list(request):
    # This will filter tasks by the current logged-in user
    tasks = Task.objects.filter(user=request.user).order_by('complete', '-created_at')
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)

# Add placeholder views for the other URLs to prevent errors
@login_required
def update_task(request, pk):
    return redirect('task-list')

@login_required
def delete_task(request, pk):
    return redirect('task-list')