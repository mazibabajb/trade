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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('code', models.CharField(blank=True, max_length=12)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_by', to='Djangoecormeceapp.affiliateuser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Djangoecormeceapp.affiliateuser')),
            ],
        ),
    ]