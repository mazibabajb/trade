# Generated by Django 4.0.3 on 2022-04-11 07:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(default='Tradebay blog posts', max_length=300)),
                ('content', models.TextField(max_length=4000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=100)),
                ('blog_img', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('is_trending', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postcategory')),
            ],
        ),
    ]
