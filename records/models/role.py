from django.db import models


class RoleType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(
        max_length=100
    )  # Monastic office name (e.g., Hostillarij, Abbot)
    role_type = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        'records.Institution', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
