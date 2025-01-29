from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Published"))

class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ValorRecord(models.Model):
    name = models.CharField(max_length=200)  # not unique as there may be more than one entry for ex. 'St Stephen's Chapel'
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='valor_records'
    )
    construction_date = models.DateField()
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='valor_records'  # Foreign key to County
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

class ReligiousOrder(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class HouseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Monastery(models.Model):
    valor_record = models.ForeignKey(
        ValorRecord, on_delete=models.CASCADE, related_name='monasteries'
    )
    religious_order = models.ForeignKey(
        ReligiousOrder, on_delete=models.CASCADE, related_name='monasteries'
    )
    house_type = models.ForeignKey(
        HouseType, on_delete=models.CASCADE, related_name='monasteries'
    )
    founded_date = models.DateField()

    class Meta:
        verbose_name_plural = 'monasteries'

    def __str__(self):
        return self.valor_record.name