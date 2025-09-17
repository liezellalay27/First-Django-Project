from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)

def update_task(request, pk):
    return render(request, 'tasks.html')

def delete_task(request, pk):
    return render(request, 'tasks.html')