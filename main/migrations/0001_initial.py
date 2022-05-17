# Generated by Django 4.0.4 on 2022-05-17 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('parent', models.BooleanField()),
                ('student', models.BooleanField()),
                ('dual_parent_student', models.BooleanField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_primary', models.CharField(max_length=50)),
                ('email_secondary', models.CharField(max_length=50)),
                ('mobile_one', models.IntegerField()),
                ('mobile_two', models.IntegerField()),
                ('phone_one', models.IntegerField()),
                ('age', models.CharField(max_length=3)),
                ('gender', models.BooleanField()),
                ('guardian', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=100)),
                ('medical_info', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=50)),
                ('tkd_program', models.CharField(
                    choices=[('BLANK', 'N/A'), ('TIGER CUB', 'Tiger Cub'), ('JR', 'Jr'), ('YOUTH', 'Youth'),
                             ('ADULT', 'Adult')], max_length=200)),
                ('xp_program', models.CharField(
                    choices=[('BLANK', 'N/A'), ('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'),
                             ('ADVANCED', 'Advanced')], max_length=100)),
                ('sc_program', models.CharField(choices=[('BLANK', 'N/A'), ('WHITE', 'White'), ('YELLOW', 'Yellow')],
                                                max_length=100)),
                ('instructor', models.BooleanField()),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
