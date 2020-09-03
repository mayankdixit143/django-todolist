from django.db import models
from django.utils import timezone

# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    deadline = models.DateTimeField(default=timezone.now)
