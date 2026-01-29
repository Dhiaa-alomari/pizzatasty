from django.db import migrations

def create_initial_tables(apps, schema_editor):
    Table = apps.get_model('booking', 'Table')
    
    capacities = [2, 2, 4, 4, 6, 6, 8, 10]
    
    for cap in capacities:
        Table.objects.create(capacity=cap)

def remove_initial_tables(apps, schema_editor):
    Table = apps.get_model('booking', 'Table')
    Table.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_initial_tables, remove_initial_tables),
    ]