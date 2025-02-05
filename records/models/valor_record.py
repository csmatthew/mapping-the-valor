from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Published"))
TYPE_CHOICES = (
    ('monastery', 'Monastery'),
    # Add other types here if needed
)


class ValorRecord(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='valor_records'
    )
    construction_date = models.DateField()
    county = models.ForeignKey(
        'records.County',
        on_delete=models.CASCADE,
        related_name='valor_records'
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='monastery'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name
