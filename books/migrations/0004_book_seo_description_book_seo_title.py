# Generated by Django 4.0.3 on 2022-05-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_book_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='seo_description',
            field=models.CharField(default='Tradebay book detail', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='seo_title',
            field=models.CharField(default='Tradebay book detail', max_length=200),
        ),
    ]
