from django.db import migrations


def create_housetype_instances(apps, schema_editor):
    HouseType = apps.get_model('valor_records', 'HouseType')
    house_type_choices = {
        1: 'Abbey',
        2: 'Priory',
        3: 'Nunnery',
    }

    for key, value in house_type_choices.items():
        HouseType.objects.get_or_create(house_type=value)


class Migration(migrations.Migration):

    dependencies = [
        ('valor_records', '0014_alter_housetype_house_type'),
    ]

    operations = [
        migrations.RunPython(create_housetype_instances),
    ]
