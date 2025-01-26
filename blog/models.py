from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import requests

STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Published"))

class ReligiousOrder(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class HouseType(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return self.name

class Post(models.Model):
    monastery_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    religious_order = models.ForeignKey(ReligiousOrder, on_delete=models.SET_NULL, null=True, blank=True)
    house_type = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True, blank=True)
    nearest_town = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, default='Unknown')
    year_founded = models.IntegerField()
    content = models.TextField(blank=True)
    coordinates = models.CharField(max_length=50, null=True, blank=True)  # Coordinates in '53.8202°N 2.4104°W' format
    created_by = models.ForeignKey(User, related_name='created_posts', on_delete=models.CASCADE, null=True, blank=True)
    last_updated_by = models.ForeignKey(User, related_name='updated_posts', on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=500, blank=True, null=True)  # For images from wikipedia

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = f"{self.name}-{self.house_type.name}" if self.house_type else self.name
            self.slug = slugify(slug_base)
        super().save(*args, **kwargs)
        if self.status == 2:  # If the post is approved
            ApprovedPost.objects.update_or_create(
                post=self,
                defaults={
                    'name': self.name,
                    'slug': self.slug,
                    'religious_order': self.religious_order,
                    'house_type': self.house_type,
                    'nearest_town': self.nearest_town,
                    'county': self.county,
                    'year_founded': self.year_founded,
                    'content': self.content,
                    'coordinates': self.coordinates,
                    'image_url': self.image_url,
                }
            )

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name, self.house_type.natural_key())

class ApprovedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='approved_version')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    religious_order = models.ForeignKey(ReligiousOrder, on_delete=models.SET_NULL, null=True, blank=True)
    house_type = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True, blank=True)
    nearest_town = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, default='Unknown')
    year_founded = models.IntegerField()
    content = models.TextField(blank=True)
    coordinates = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name, self.house_type.natural_key())

