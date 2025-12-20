from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)   # set once at creation
    updated_at = models.DateTimeField(auto_now=True)       # update every save

    def __str__(self):
        return f"{self.title} ({'done' if self.completed else 'todo'})"



    