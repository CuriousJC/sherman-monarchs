# Generated by Django 4.2.6 on 2023-10-16 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monarch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('aspect', models.CharField(max_length=200)),
            ],
        ),
    ]
