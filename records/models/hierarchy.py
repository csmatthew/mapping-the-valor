from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_url_name(self):
        return 'province_detail'


class Diocese(models.Model):
    name = models.CharField(max_length=100, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url_name(self):
        return 'diocese_detail'


class Archdeaconry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Archdeaconries'

    def __str__(self):
        return self.name

    def get_url_name(self):
        return 'archdeaconry_detail'


class Deanery(models.Model):
    name = models.CharField(max_length=100, unique=True)
    archdeaconry = models.ForeignKey(Archdeaconry, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Deaneries'

    def __str__(self):
        return self.name

    def get_url_name(self):
        return 'deanery_detail'


class Parish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    deanery = models.ForeignKey(Deanery, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Parishes'

    def __str__(self):
        return self.name

    def get_url_name(self):
        return 'parish_detail'
