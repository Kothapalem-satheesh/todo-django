
# from http.client import HTTPResponse
# from django.shortcuts import get_object_or_404,redirect,render # type: ignore
# from .models import Task  


# def addTask(request):
#     task=request.POST['task']
#     Task.objects.create(task=task)   
#     return redirect('home')


# def mark_as_done(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_completed = True 
#     task.save()
#     return redirect('home')

    
# from django.shortcuts import redirect, render
# from .models import Task


# def addTask(request):
    
#     tasks = Task.objects.all()
#     if request.method == "POST":
#         task = request.POST.get('task')

#         if task:
#             Task.objects.create(task=task)

#     return redirect('home')


# def mark_as_done(request, pk):
#     task = Task.objects.get(id=pk)
#     task.is_completed = True
#     task.save()

#     return redirect('home')


from django.shortcuts import redirect, render
from .models import Task
from django.shortcuts import get_object_or_404

def home(request):

    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'tasks': tasks
    })



def addTask(request):

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(task=task)

    return redirect('home')



def mark_as_done(request, pk):

    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()

    return redirect('home')


def mark_as_Undone(request, pk):

    task = Task.objects.get(id=pk)
    task.is_completed = False
    task.save()

    return redirect('home')


# def edit_task(request,pk):
#     get_task=get_object_or_404(Task,pk=pk)
#     if request.method==POST:
#         return
#     else:
#         context={
#             'get_task':get_task
#         }
#     return render(request,'edit_task.html',context)
 
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        new_task = request.POST.get('task')

        if new_task:
            task.task = new_task
            task.save()
            return redirect('home')

    context = {
        'task': task
    }

    return render(request, 'edit_task.html', context)




def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')