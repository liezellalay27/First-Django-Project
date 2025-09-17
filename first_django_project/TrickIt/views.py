from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def task_list(request):
    # Your logic for displaying a list of tasks
    return render(request, 'home.html') # Or whatever template you want to use for the task list

def update_task(request, pk):
    # Your logic for updating a task
    return render(request, 'home.html') # This should be a template for updating a task

def delete_task(request, pk):
    # Your logic for deleting a task
    return render(request, 'home.html') # This should be a confirmation page for deleting a task