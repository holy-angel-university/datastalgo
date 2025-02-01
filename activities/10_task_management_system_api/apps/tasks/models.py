from django.db import models
from django.contrib.auth.models import User
from .choices import STATUS_CHOICES
from helpers.generate_id import generate_unique_id


class Task(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=generate_unique_id)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
