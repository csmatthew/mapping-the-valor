from django.db import models


class ValorRecord(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(default='')

    def __str__(self):
        return self.name
