


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task

# Home page - redirects to login or dashboard based on authentication
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Changed from dashboard(request) to redirect
    return redirect('login')

# Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

# Register View
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        # Validate passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
        
        # Check if email already exists
        if email and User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'register.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email if email else '',
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            
            # Auto login after registration
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
            
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'register.html')
    
    return render(request, 'register.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# Dashboard View (Protected) - This is your home.html
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(user=request.user, is_completed=True).order_by('-updated_at')
    
    return render(request, 'home.html', {  # Changed from 'index.html' to 'home.html'
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'user': request.user
    })

# Add Task (Protected)
@login_required
def addTask(request):
    if request.method == "POST":
        task_text = request.POST.get('task')
        
        if task_text:
            # Get additional fields from the form
            category = request.POST.get('category', 'work')
            priority = request.POST.get('priority', 'medium')
            due_date = request.POST.get('due_date', None)
            
            Task.objects.create(
                user=request.user,
                task=task_text,
                category=category,
                priority=priority,
                due_date=due_date if due_date else None
            )
            messages.success(request, 'Task added successfully!')
        else:
            messages.error(request, 'Task cannot be empty!')
    
    return redirect('dashboard')

# Mark as Done (Protected)
@login_required
def mark_as_done(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.is_completed = True
    task.save()
    messages.success(request, 'Task marked as completed!')
    return redirect('dashboard')

# Mark as Undone (Protected)
@login_required
def mark_as_Undone(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    task.is_completed = False
    task.save()
    messages.success(request, 'Task reactivated!')
    return redirect('dashboard')

# Edit Task (Protected)
@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        new_task = request.POST.get('task')
        
        if new_task:
            task.task = new_task
            
            # Update additional fields if provided
            task.category = request.POST.get('category', task.category)
            task.priority = request.POST.get('priority', task.priority)
            due_date = request.POST.get('due_date')
            if due_date:
                task.due_date = due_date
            
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Task cannot be empty!')

    context = {'task': task}
    return render(request, 'edit_task.html', context)

# Delete Task (Protected)
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('dashboard')