from django.db import models


class Currency(models.Model):
    name = models.CharField(
        max_length=100
        )  # e.g., 'Pounds', 'Shillings', 'Pence'
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Value(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        'records.Institution', on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True, null=True
    )  # Description for the monetary value

    def __str__(self):
        return f"{self.amount} {self.currency.symbol}"
