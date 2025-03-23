from django.db import models
from django.contrib.auth.models import User


class ValorText(models.Model):
    valor_record = models.ForeignKey(
        'ValorRecord', on_delete=models.CASCADE, related_name='texts'
    )
    original_text = models.TextField()  # Stores the original text
    # (Latin/archaic English)
    translation = models.TextField(
        blank=True, null=True
    )  # Optional field for the translation
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='created_valor_texts'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Text for {self.valor_record.name} "
            f"(Created: {self.date_created})"
        )
