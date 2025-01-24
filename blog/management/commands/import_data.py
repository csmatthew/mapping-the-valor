# blog/management/commands/import_data.py
import csv
from django.core.management.base import BaseCommand
from blog.models import Post, ReligiousOrder

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def handle(self, *args, **kwargs):
        with open('data_import_manage/Cistercian Abbeys - Sheet12.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                religious_order, created = ReligiousOrder.objects.get_or_create(name=row['religious_order'])
                post, created = Post.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'religious_order': religious_order,
                        'nearest_town': row['nearest_town'],
                        'county': row['county'],
                        'year_founded': row['year_founded'],
                        'content': row['content'],
                        'coordinates': row['coordinates'],
                        'status': 2,
                    }
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))