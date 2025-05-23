# Generated by Django 5.1.5 on 2025-02-28 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deanery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deanery_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(choices=[('Monastery', 'Monastery'), ('Collegiate Church', 'Collegiate Church'), ('Rectory', 'Rectory')], max_length=50)),
                ('deanery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valor_records.deanery')),
            ],
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(choices=[('Abbey', 'Abbey'), ('Priory', 'Priory'), ('Nunnery', 'Nunnery')], max_length=50)),
                ('institution', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='valor_records.institution')),
            ],
        ),
    ]
