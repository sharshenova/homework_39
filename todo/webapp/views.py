from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task

def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def create_task_view(request):
    task = Task.objects.create (
        name = request.POST.get('task_name')
    )
    return redirect('task_index')


def delete_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={
            'task': task
        })
    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            task.delete()
        return redirect('task_index')


def edit_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == "GET":
        return render(request, 'task_edit.html', context={
            'task': task
        })
    elif request.method == "POST":
        task.name = request.POST.get('task_name')
        task.status = request.POST.get('task_status')
        task.save()
        return redirect('task_index')


def do_task_view(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)

    if request.method == "GET":
        return redirect('task_index')

    elif request.method == "POST":
        task.status = 'done'
        task.save()
        return redirect('task_index')

def delete_all_view(request):
    if request.method == 'GET':
        done_tasks = Task.objects.filter(status='done')
        context = {
            'done_tasks': done_tasks
        }

        return render(request, 'delete_all.html', context)

    elif request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            done_tasks = Task.objects.filter(pk__in=request.POST.getlist('task_pks'))

            for task in done_tasks:
                task.delete()

        return redirect('task_index')


