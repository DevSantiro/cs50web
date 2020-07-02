from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    newyear = now.day == 1 and now.month == 1

    return render(request, "tarefas/index.html", {'newyear': newyear})
