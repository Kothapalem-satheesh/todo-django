


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todo.models import Task

@login_required  # Add this decorator
def home(request):
    if request.user.is_authenticated:
        # Show only the logged-in user's tasks
        tasks = Task.objects.filter(user=request.user, is_completed=False).order_by("-updated_at")
        completed_tasks = Task.objects.filter(user=request.user, is_completed=True)
        
        # Calculate productivity score
        total_tasks = tasks.count() + completed_tasks.count()
        if total_tasks > 0:
            productivity_score = int((completed_tasks.count() / total_tasks) * 100)
        else:
            productivity_score = 0
            
        context = {
            'tasks': tasks,
            'completed_tasks': completed_tasks,
            'productivity_score': productivity_score,
            'user': request.user
        }
    else:
        # This shouldn't happen because of @login_required, but just in case
        return redirect('login')
    
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})