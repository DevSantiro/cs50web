from django.shortcuts import render

# Create your views here.

task = ['Rodrigo', 'Santiago', 'Claro', 'Filho']

def index(request):
    
    return render(request, 'task/index.html', {'tasks': task})


def addTask(request):

    return render(request, 'task/addTask.html', {'tasks': task})
    