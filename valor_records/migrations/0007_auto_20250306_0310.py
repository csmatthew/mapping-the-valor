from django.db import migrations


def update_record_type(apps, schema_editor):
    ValorRecord = apps.get_model('valor_records', 'ValorRecord')
    ValorRecord.objects.filter(
        record_type='Collegiate Church'
    ).update(record_type='Collegiate')


class Migration(migrations.Migration):

    dependencies = [
        ('valor_records', '0006_alter_valorrecord_record_type'),
    ]

    operations = [
        migrations.RunPython(update_record_type),
    ]
