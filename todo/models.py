from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
            ('low','low'),
            ('medium','medium'),
            ('high','high')
     ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
    )
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title