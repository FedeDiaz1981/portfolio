# Generated by Django 5.1.7 on 2025-03-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='link',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
    ]
