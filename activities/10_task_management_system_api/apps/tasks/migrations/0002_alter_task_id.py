# Generated by Django 5.1.5 on 2025-02-01 04:51

import helpers.generate_id
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="id",
            field=models.CharField(
                default=helpers.generate_id.generate_unique_id,
                max_length=8,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
