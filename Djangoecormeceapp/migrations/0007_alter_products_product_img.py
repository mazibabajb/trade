# Generated by Django 4.0.3 on 2022-05-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangoecormeceapp', '0006_rename_description_products_seo_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_img',
            field=models.ImageField(default='default-car.png', upload_to='cars'),
        ),
    ]
