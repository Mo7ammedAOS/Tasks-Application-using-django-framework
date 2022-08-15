from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# (Adding the saved tasks)

def mainHome(request):

    task_list = Task.objects.order_by('id')

    form = TaskForm()

    context = {'task_list' : task_list,'form':form}

    return render(request, 'Tasks/task.html',context)

# (Adding Tasks)
def addinItems(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        data = request.POST['text']
        add_new_task = Task(added_task = data)
        add_new_task.save()
    return redirect('home')

# (Tasks completed)

def taskCompleteness(request,pk):
    task_completed = Task.objects.get(id = pk)
    task_completed.check_task = True
    task_completed.save()

    return redirect('home')

# (To delete completed tasks only)

def deleteCompleted(request):
    Task.objects.filter(check_task__exact=True).delete()

    return redirect('home')

# (To delete all Tasks)

def deleteAll(request):
    Task.objects.all().delete()

    return redirect('home')