# Generated by Django 5.1.7 on 2025-03-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conference', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
