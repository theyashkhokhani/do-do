from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ToDo(models.Model):
    COMPLETION_STATUS = [
        ('Open', 'Pending'),
        ('Close', 'Completed'),
    ]
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True)
    tag = models.CharField(max_length=19)
    description = models.CharField(max_length=240)
    status = models.CharField(max_length=10, choices=COMPLETION_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Card(models.Model):
    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)