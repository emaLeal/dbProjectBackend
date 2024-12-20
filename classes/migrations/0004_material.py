# Generated by Django 5.1.1 on 2024-11-26 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_attendance_class_id_attendance_hour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('file_id', models.BigAutoField(default=True, primary_key=True, serialize=False, unique=True)),
                ('file_name', models.CharField(default='', max_length=100)),
                ('file_path', models.CharField(default='', max_length=100)),
                ('file_type', models.CharField(default='', max_length=10)),
                ('class_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
            ],
        ),
    ]
