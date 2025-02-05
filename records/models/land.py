from django.db import models


class LandType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Land(models.Model):
    name = models.CharField(
        max_length=200
    )  # Not unique, as there could be many lands with similar names
    land_type = models.ForeignKey(LandType, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        'records.institution', on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
