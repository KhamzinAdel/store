# Generated by Django 4.1.4 on 2023-02-02 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.AddField(
            model_name='reviews',
            name='star_rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.starrating'),
            preserve_default=False,
        ),
    ]