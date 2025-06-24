import uuid

from django.contrib.auth.models import User
from django.db import models

class UUID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Todos(UUID):
    class Status(models.TextChoices):
        Todo= 'todo', 'Todo'
        Doing= 'doing', 'Doing'
        Done= 'done', 'Done'

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(max_length=10, choices=Status.choices)

    class Meta:
        unique_together = ('user',)
        ordering = ['-created_at']