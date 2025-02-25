from django.db import models


class Monastery(models.Model):
    HOUSE_TYPE_CHOICES = [
        ('Abbey', 'Abbey'),
        ('Priory', 'Priory'),
        ('Convent', 'Convent'),
        ('Friary', 'Friary'),
    ]

    RELIGIOUS_ORDER_CHOICES = [
        ('Benedictines', 'Benedictines'),
        ('Cistercians', 'Cistercians'),
        ('Franciscans', 'Franciscans'),
        ('Dominicans', 'Dominicans'),
    ]

    house_type = models.CharField(
        max_length=50,
        choices=HOUSE_TYPE_CHOICES,
        null=True,
        blank=True
    )
    religious_order = models.CharField(
        max_length=50,
        choices=RELIGIOUS_ORDER_CHOICES,
        null=True,
        blank=True
    )
    monastery_name = models.CharField(max_length=255, null=True, blank=True)
    abbot = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.monastery_name
