# Generated by Django 5.0.4 on 2024-07-25 14:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_rename_year_book_publish_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
