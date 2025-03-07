from django.db import models


class Deanery(models.Model):
    deanery_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.deanery_name

    class Meta:
        verbose_name_plural = 'deaneries'
