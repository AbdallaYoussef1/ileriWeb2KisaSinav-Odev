# Generated by Django 5.0.1 on 2024-01-10 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
    ]
