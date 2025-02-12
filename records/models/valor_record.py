from django.db import models
from django.utils import timezone


class ValorRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('Parish', 'Parish'),
        ('Religious House', 'Religious House'),
        ('College', 'College'),
    ]

    name = models.CharField(max_length=255)
    content = models.TextField(default='')
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    record_type = models.CharField(
        max_length=50,
        choices=RECORD_TYPE_CHOICES,
        default='Parish'
    )

    def __str__(self):
        return self.name
