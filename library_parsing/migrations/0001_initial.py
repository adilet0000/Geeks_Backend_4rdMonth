# Generated by Django 4.2.11 on 2025-01-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookParser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("info", models.CharField(max_length=250)),
                ("href", models.URLField()),
            ],
        ),
    ]
