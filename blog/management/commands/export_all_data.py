# blog/management/commands/export_all_data.py
import csv
import os
from django.core.management.base import BaseCommand
from django.apps import apps
from django.conf import settings

class Command(BaseCommand):
    help = 'Export data from all models to CSV files'

    def handle(self, *args, **kwargs):
        # Directory to save the CSV files
        export_dir = os.path.join(settings.BASE_DIR, 'exports')
        os.makedirs(export_dir, exist_ok=True)

        # Get all models
        all_models = apps.get_models()

        for model in all_models:
            model_name = model.__name__
            file_path = os.path.join(export_dir, f'{model_name}.csv')

            # Get all fields of the model
            field_names = [field.name for field in model._meta.fields]

            # Write data to CSV file
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(field_names)  # Write header

                for instance in model.objects.all():
                    row = [getattr(instance, field) for field in field_names]
                    writer.writerow(row)

            self.stdout.write(self.style.SUCCESS(f'Data exported successfully for model: {model_name}'))

        self.stdout.write(self.style.SUCCESS('All data exported successfully'))