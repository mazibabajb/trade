# Generated by Django 4.0.3 on 2022-05-02 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Djangoecormeceapp', '0005_alter_products_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='description',
            new_name='seo_description',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='title',
            new_name='seo_title',
        ),
    ]
