# Generated by Django 4.0.1 on 2022-01-24 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model_location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('floor_of_flat', models.CharField(blank=True, max_length=255, null=True)),
                ('number_of_rooms', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='model_location.city')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'flat',
                'verbose_name_plural': 'flats',
            },
        ),
    ]
