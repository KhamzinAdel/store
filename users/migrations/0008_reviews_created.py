# Generated by Django 4.1.4 on 2023-02-10 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_starrating_reviews_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 10, 14, 21, 5, 411058, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]