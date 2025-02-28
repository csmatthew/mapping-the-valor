from django.db import models

# Create your models here.


class Deanery(models.Model):
    deanery_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.deanery_name

    class Meta:
        verbose_name_plural = 'deaneries'


class Institution(models.Model):
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

    institution = models.OneToOneField(Institution, on_delete=models.CASCADE)
    house_type = models.CharField(max_length=50, choices=HOUSE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.institution.name} - {self.house_type}"
