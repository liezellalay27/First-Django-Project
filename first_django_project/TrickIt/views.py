from django.shortcuts import render

def task_list(request):
    # Your view logic goes here
    # Render the existing home.html template
    return render(request, 'TrickIt/home.html')