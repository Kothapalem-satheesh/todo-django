# from django.http import HttpResponse
# from django.shortcuts import redirect,render
# from .models import Task
# # Create your views here.
# def addTask(request):
#     task=request.POST['task']
#     task.object.create(task=task)
#     return redirect('home')


from django.shortcuts import redirect
from .models import Task   # ✅ correct model name


def addTask(request):

    if request.method == "POST":

        task = request.POST.get('task')

        if task:
            Task.objects.create(task=task)   # ✅ CORRECT

    return redirect('home')
