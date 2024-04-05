from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from todo.forms import TaskForm
from .models import Task

# list all the tasks
def tasklist(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return  render(request, 'todo/tasklist.html',context)
    

# add a new task to the database or update an existing one
def taskadd(request, pk=None):
    task = None
    if pk:
        task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('list'))
    else:
        form = TaskForm(instance=task)

    context = {'form':form, 'task':task}

    return render(request, 'todo/taskadd.html', context)

def taskdelete(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        # Redirect to the home page after deleting.
        return redirect(reverse_lazy('list'))
    
    context = {'task':task}

    return render(request, 'todo/taskdelete.html', context)

def taskoperation(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()    
        # Redirect to the home page after deleting.
        return redirect(reverse_lazy('list'))