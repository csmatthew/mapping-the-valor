from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .deanery import Deanery
from .house_type import HouseType
from .religious_order import ReligiousOrder


class ValorRecord(models.Model):
    TYPE_CHOICES_DICT = {
        'Monastery': 'Monastery',
        'Collegiate': 'Collegiate',
        'Rectory': 'Rectory',
    }

    TYPE_CHOICES = [(key, value) for key, value in TYPE_CHOICES_DICT.items()]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    # General
    name = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    dedication = models.CharField(blank=True, max_length=255, null=True)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending'
    )

    # Monastic
    house_type = models.ForeignKey(
        HouseType, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='house_records'
    )
    religious_order = models.ForeignKey(
        ReligiousOrder, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='religious_order_records'
    )

    # Geographical Coordinates
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    # Reference data
    source_ref_vol = models.IntegerField(null=True, blank=True)
    source_ref_page = models.IntegerField(null=True, blank=True)

    # User data
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
        if not self.pk and user:
            self.created_by = user
        if user:
            self.last_edited_by = user

        # Always regenerate the slug based on the current name and record_type
        if self.record_type == 'Monastery' and self.house_type:
            slug_base = f"{self.name}-{self.house_type.house_type}"
        else:
            slug_base = f"{self.name}-{self.record_type}"
        self.slug = slugify(slug_base)
        print(f"Generated slug: {self.slug}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
