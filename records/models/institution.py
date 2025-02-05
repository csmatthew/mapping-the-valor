from django.db import models
from django.contrib.auth.models import User
from .valor_record import ValorRecord


class ReligiousOrder(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class HouseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=200)
    valor_record = models.ForeignKey(
        ValorRecord,
        on_delete=models.CASCADE,
        related_name='institutions'
    )
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Draft', 'Draft'),
                 ('Pending Approval', 'Pending Approval'),
                 ('Approved', 'Approved')], default='Draft'
    )
    claimed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='claimed_institutions'
    )

    def __str__(self):
        return self.name


class AuditLog(models.Model):
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE,
        related_name='audit_logs'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    # E.g., "Created", "Edited", "Submitted for Approval"
    changes = models.TextField()
    # Store what was changed, can be serialized or manually added
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Change to {self.institution.name} by {self.user} "
                f"on {self.created_on}")


class Comment(models.Model):
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.institution.name}"
