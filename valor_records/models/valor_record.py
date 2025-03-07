from django.db import models
from django.contrib.auth.models import User
from .deanery import Deanery
from .house_type import HouseType


class ValorRecord(models.Model):
    TYPE_CHOICES_DICT = {
        'Monastery': 'Monastery',
        'Collegiate': 'Collegiate',
        'Rectory': 'Rectory',
    }

    TYPE_CHOICES = [(key, value) for key, value in TYPE_CHOICES_DICT.items()]

    name = models.CharField(max_length=255, unique=True)
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    house_type = models.ForeignKey(
        HouseType, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='valor_records'
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='created_valor_records'
    )
    last_edited_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='edited_valor_records'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if not self.pk:
            if user:
                self.created_by = user
        if user:
            self.last_edited_by = user  # Update last_edited_by on every save

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
