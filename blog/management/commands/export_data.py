# blog/management/commands/export_data.py
import csv
from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Export data to a CSV file'

    def handle(self, *args, **kwargs):
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'religious_order', 'nearest_town', 'county', 'year_founded', 'content', 'coordinates']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in Post.objects.all():
                writer.writerow({
                    'name': post.name,
                    'religious_order': post.religious_order.name if post.religious_order else '',
                    'nearest_town': post.nearest_town,
                    'county': post.county,
                    'year_founded': post.year_founded,
                    'content': post.content,
                    'coordinates': post.coordinates,
                })
        self.stdout.write(self.style.SUCCESS('Data exported successfully'))