# Generated by Django 4.1.4 on 2023-01-28 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
    ]
