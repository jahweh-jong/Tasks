from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import CreateTaskForm

@login_required
def index(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            
            return redirect('tasks:index')
    else:
        form = CreateTaskForm()

    tasks = Task.objects.filter(created_by = request.user)
    done_tasks = [task for task in tasks if task.is_done]
    undone_tasks = [task for task in tasks if not task.is_done]
    context = {
        'form': form,
        'done_tasks' : done_tasks,
        'undone_tasks': undone_tasks
    }
    return render(request, 'tasks/index.html', context=context)

@login_required
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.delete()

    return redirect('tasks:index')

@login_required
def done(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.is_done = True
    task.save()

    return redirect('tasks:index')

@login_required
def undone(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.is_done = False
    task.save()

    return redirect('tasks:index')
