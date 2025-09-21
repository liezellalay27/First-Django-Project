from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task # This is the only import needed for Task
from .forms import TaskForm
# Make sure you import the Task model
from .models import Task 

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('complete', '-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('task-list')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks.html', context)

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    
    context = {'form': form}
    return render(request, 'update_task.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    
    context = {'task': task}
    return render(request, 'delete_task.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("task-list")
    else:
        form = UserCreationForm()
    # Update this line to include the 'registration' folder
    return render(request, "registration/register.html", {"form": form}) 