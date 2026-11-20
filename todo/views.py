
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render


from .forms import TaskForm
from .models import Task

def landing(request):
    return render(request, 'todo/landing.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'todo/register.html', {'form': form})

@login_required
def task_list(request):
    tasks=Task.objects.all()
    return render(request,'todo/task_list.html',{'tasks':tasks})


def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request,'todo/add_task.html',{'form':form})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()

    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()

    return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})