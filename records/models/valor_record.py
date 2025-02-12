from django.db import models
from django.utils import timezone
from .hierarchy import Province, Diocese, Archdeaconry, Deanery


class ValorRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('Parish', 'Parish'),
        ('Religious House', 'Religious House'),
        ('College', 'College'),
    ]

    name = models.CharField(max_length=255)
    content = models.TextField(default='')
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    record_type = models.CharField(
        max_length=50,
        choices=RECORD_TYPE_CHOICES,
        default='Parish'
    )
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, null=True, blank=True
    )
    diocese = models.ForeignKey(
        Diocese, on_delete=models.CASCADE, null=True, blank=True
    )
    archdeaconry = models.ForeignKey(
        Archdeaconry, on_delete=models.CASCADE, null=True, blank=True
    )
    deanery = models.ForeignKey(
        Deanery, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
