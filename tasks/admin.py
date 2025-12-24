from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'priority', 'is_completed', 'due_date', 'created_at')
    list_filter = ('is_completed', 'priority', 'due_date', 'owner')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
