# Generated by Django 5.1.3 on 2024-11-27 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_rename_grades_lessongrades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school_app.room'),
            preserve_default=False,
        ),
    ]
