from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from . models import Tasks
# Create your views here.


def list_tasks_item(request):
    content = {'tasks': Tasks.objects.all()}
    return render(request, 'tasks/tasks_list.html', content)


def insert_tasks_item(request: HttpRequest):
    task = Tasks(content=request.POST['content'])
    task.save()
    return redirect('/tasks/')


def delete_tasks_item(request, task_id):
    task_to_delete = Tasks.objects.get(id=task_id)
    task_to_delete.delete()
    return redirect('/tasks/')
