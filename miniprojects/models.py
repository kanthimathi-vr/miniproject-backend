from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class MiniProject(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("inprogress", "In Progress"),
        ("complete", "Complete"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_projects')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="pending")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} assigned to {self.assigned_to.email}"
