# Generated by Django 3.2.4 on 2023-03-17 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20230317_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.SmallIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
