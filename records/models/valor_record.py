from django.db import models
from .hierarchy import Province, Diocese, Archdeaconry, Deanery, Parish
from .monastery import Monastery


class ValorRecord(models.Model):
    RECORD_TYPE_CHOICES = [
        ('Monastery', 'Monastery'),
        ('College', 'College'),
        ('Rectory', 'Rectory'),
    ]

    name = models.CharField(max_length=255)
    content = models.TextField(default='')
    slug = models.SlugField(unique=True, default='default-slug')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    record_type = models.CharField(
        max_length=50,
        choices=RECORD_TYPE_CHOICES,
        default='Monastery'
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
    parish = models.ForeignKey(
        Parish, on_delete=models.CASCADE, null=True, blank=True
    )
    monastery = models.ForeignKey(
        Monastery, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
