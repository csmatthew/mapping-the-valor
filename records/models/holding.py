from django.db import models
from .valor_record import ValorRecord


class Holding(models.Model):
    valor_record = models.ForeignKey(
        ValorRecord, on_delete=models.CASCADE, related_name='holdings'
    )
    description = models.TextField()
    pounds = models.IntegerField(null=True, blank=True)
    shillings = models.IntegerField(null=True, blank=True)
    pence = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.description
