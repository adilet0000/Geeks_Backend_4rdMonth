# Generated by Django 4.2.11 on 2025-01-28 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название рецепта"),
                ),
                ("description", models.TextField(verbose_name="Описание рецепта")),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название ингредиента"
                    ),
                ),
                ("quantity", models.FloatField(verbose_name="Количество")),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("г", "граммы"),
                            ("кг", "килограммы"),
                            ("мл", "миллилитры"),
                            ("л", "литры"),
                            ("шт", "штуки"),
                        ],
                        max_length=10,
                        verbose_name="Единица измерения",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients",
                        to="recipes.recipe",
                    ),
                ),
            ],
        ),
    ]
