# Generated by Django 2.2.9 on 2020-01-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200117_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
