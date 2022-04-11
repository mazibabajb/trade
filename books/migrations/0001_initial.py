# Generated by Django 4.0.3 on 2022-04-11 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Djangoecormeceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('profile', models.ImageField(default='default-car.png', upload_to='cars')),
                ('dob', models.DateField()),
                ('background', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_slug', models.SlugField(blank=True)),
                ('title', models.CharField(max_length=200)),
                ('auther', models.CharField(max_length=200)),
                ('book_file', models.FileField(default='default-car.png', upload_to='cars')),
                ('book_thumbnail', models.ImageField(default='default-car.png', upload_to='cars')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Djangoecormeceapp.merchantuser')),
            ],
        ),
    ]
