# Generated by Django 4.0.3 on 2022-05-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomo', '0009_propertyviewcount_property_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='seo_description',
            field=models.CharField(default='Tradebay property detail', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='seo_title',
            field=models.CharField(default='Tradebay property detail', max_length=200),
        ),
    ]
