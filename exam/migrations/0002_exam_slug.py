# Generated by Django 4.0.4 on 2022-05-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
