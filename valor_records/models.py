from django.db import models
from django.contrib.auth.models import User


class Deanery(models.Model):
    deanery_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.deanery_name

    class Meta:
        verbose_name_plural = 'deaneries'


class ValorRecord(models.Model):
    MONASTERY = 'Monastery'
    COLLEGIATE = 'Collegiate'
    RECTORY = 'Rectory'

    TYPE_CHOICES = [
        (MONASTERY, 'Monastery'),
        (COLLEGIATE, 'Collegiate'),
        (RECTORY, 'Rectory'),
    ]

    name = models.CharField(max_length=255, unique=True)
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
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


class HouseType(models.Model):
    ABBEY = 'Abbey'
    PRIORY = 'Priory'
    NUNNERY = 'Nunnery'

    HOUSE_TYPE_CHOICES = [
        (ABBEY, 'Abbey'),
        (PRIORY, 'Priory'),
        (NUNNERY, 'Nunnery'),
    ]

    valor_record = models.OneToOneField(ValorRecord, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=50, choices=HOUSE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.valor_record.name} - {self.house_type}"
