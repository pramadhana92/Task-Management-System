from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['id', 'title', 'description', 'is_complete']
    search_fields = ['id', 'title', 'description']

admin.site.register(Task, TaskAdmin)