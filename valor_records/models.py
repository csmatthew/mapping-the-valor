from django.db import models
from django.core.exceptions import ValidationError


class Deanery(models.Model):
    deanery_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.deanery_name

    class Meta:
        verbose_name_plural = 'deaneries'


class ValorRecord(models.Model):
    MONASTERY = 'Monastery'
    COLLEGIATE_CHURCH = 'Collegiate Church'
    RECTORY = 'Rectory'

    TYPE_CHOICES = [
        (MONASTERY, 'Monastery'),
        (COLLEGIATE_CHURCH, 'Collegiate Church'),
        (RECTORY, 'Rectory'),
    ]

    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.type == self.MONASTERY:
            if not hasattr(self, 'housetype'):
                raise ValidationError(
                    'A Monastery must have an associated House type.'
                )


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
