from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"), (2, "Pending Approval"))

class ReligiousOrder(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    monastery_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    religious_order = models.ForeignKey(ReligiousOrder, on_delete=models.SET_NULL, null=True, blank=True)
    nearest_town = models.CharField(max_length=200, default='Unknown')
    county = models.CharField(max_length=200, default='Unknown')
    year_founded = models.IntegerField()
    content = models.TextField()
    coordinates = models.CharField(max_length=50, null=True, blank=True)  # New field
    created_by = models.ForeignKey(User, related_name='created_posts', on_delete=models.CASCADE)
    last_updated_by = models.ForeignKey(User, related_name='updated_posts', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name