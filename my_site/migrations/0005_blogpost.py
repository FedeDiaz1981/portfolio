# Generated by Django 5.1.7 on 2025-03-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0004_crecimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('excerpt', models.TextField()),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
