from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import requests

STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Published"))

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
    house_type = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True, blank=True)
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
            slug_base = f"{self.name}-{self.house_type.name if self.house_type else ''}"
            self.slug = slugify(slug_base)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return self.name

class ApprovedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='approved_version')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    house_type = models.ForeignKey('HouseType', on_delete=models.SET_NULL, null=True, blank=True)
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
        house_type_key = self.house_type.natural_key() if self.house_type else None
        return (self.name, house_type_key)
    

class FinancialDetail(models.Model):
    post = models.ForeignKey(Post, related_name='financial_details', on_delete=models.CASCADE)
    holding_title = models.CharField(max_length=200, blank=True, null=True)
    holding_pounds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    holding_shillings = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    holding_pence = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        holding_title = self.holding_title or "No title"
        holding_pounds = self.holding_pounds or 0
        holding_shillings = self.holding_shillings or 0
        holding_pence = self.holding_pence or 0
        return f"{holding_title} - {holding_pounds} pounds, {holding_shillings} shillings, {holding_pence} pence"

