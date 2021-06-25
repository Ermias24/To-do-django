from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form, 'tasks':tasks}
    return render(request, 'task.html', context)

def updateTask(request, id):
    task = Task.objects.get(id = id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form' : form}
    return render(request, 'updatetask.html', context)

def deleteTask(request, id):
    item = Task.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'delete.html', context)