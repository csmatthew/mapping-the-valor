from django.db import models
from django.utils import timezone


class ValorRecord(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(default='')
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
