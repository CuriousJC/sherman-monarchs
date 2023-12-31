# Generated by Django 4.2.6 on 2023-11-12 14:34

from django.db import migrations
from django.core.management import call_command

def load_initial_data(apps, schema_editor):
    call_command('loaddata', 'monarchsite/fixtures/initial_data.json')

class Migration(migrations.Migration):

    dependencies = [
        ('monarchsite', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
