from django.db import models


class SourceRef(models.Model):
    source_ref_vol = models.IntegerField()
    source_ref_page = models.IntegerField()

    def __str__(self):
        return f"Vol {self.source_ref_vol}, p. {self.source_ref_page}"
