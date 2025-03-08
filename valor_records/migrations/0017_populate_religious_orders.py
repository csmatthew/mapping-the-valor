from django.db import migrations

def populate_religious_orders(apps, schema_editor):
    ReligiousOrder = apps.get_model('valor_records', 'ReligiousOrder')
    RELIGIOUS_ORDER_CHOICES_DICT = {
        1: 'Augustinian',
        2: 'Benedictine',
        3: 'Carthusian',
        4: 'Cistercian',
        5: 'Cluniac',
        6: 'Dominican',
        7: 'Franciscan',
        8: 'Gilbertine',
        9: 'Knights Hospitaller',
        10: 'Premonstratensian',
        11: 'Trinitarian',
    }

    for key, value in RELIGIOUS_ORDER_CHOICES_DICT.items():
        ReligiousOrder.objects.get_or_create(religious_order=key)

class Migration(migrations.Migration):

    dependencies = [
        ('valor_records', '0016_remove_religiousorder_valor_record_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_religious_orders),
    ]
