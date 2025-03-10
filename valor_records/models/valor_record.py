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

    # General
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)

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
        if not self.pk:
            if user:
                self.created_by = user
        if user:
            self.last_edited_by = user

        if not self.slug:
            slug_base = f"{self.name}-"
            if self.house_type:
                slug_base += f"{self.house_type.house_type}"
            self.slug = slugify(slug_base)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
