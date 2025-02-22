from django.db import models


TODOS_STATUS_CHOICES = [
    ("pending", "Pending"),
    ("completed", "Completed"),
]


class Todo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=255, choices=TODOS_STATUS_CHOICES, default="pending"
    )

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
