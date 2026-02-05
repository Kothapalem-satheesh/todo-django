



from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Add user field first
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Your existing fields
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Add priority and category fields (optional but recommended)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('health', 'Health'),
        ('learning', 'Learning'),
        ('other', 'Other'),
    ]
    
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium'
    )
    
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='work'
    )
    
    # Optional: Add due date field
    due_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.task
    
    class Meta:
        ordering = ['-created_at']  # Show newest tasks first