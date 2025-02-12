from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Diocese(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Archdeaconry(models.Model):
    name = models.CharField(max_length=255)
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Deanery(models.Model):
    name = models.CharField(max_length=255)
    archdeaconry = models.ForeignKey(Archdeaconry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
