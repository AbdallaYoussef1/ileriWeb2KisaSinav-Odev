# Generated by Django 5.0.1 on 2024-01-08 13:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]