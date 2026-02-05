from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    search_fields=('Tasks',)
    list_display=('task','is_completed','updated_at')
admin.site.register(Task,TaskAdmin)
# Register your models here.
