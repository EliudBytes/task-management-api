# tasks/models.py

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # The user who owns the task (linked to the Django user model)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Task details
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # Status and scheduling
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    
    # Priority choices
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium',
    )

    class Meta:
        # Order tasks by due date, then by priority (descending)
        ordering = ['due_date', '-priority'] # Note: You can't use '-' on a CharField for priority unless custom sorting is implemented, let's keep it simple for now:
        # ordering = ['due_date', 'priority'] 

    def __str__(self):
        return self.title