# Generated by Django 4.2.17 on 2025-01-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.CharField(
                default="Автор не указан", max_length=100, verbose_name="Укажите автора"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="author_email",
            field=models.EmailField(
                blank=True,
                default="Почта автора не указана",
                max_length=254,
                verbose_name="Укажите почту автора",
            ),
        ),
        migrations.CreateModel(
            name="Review",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("comment", models.TextField(verbose_name="Ваш комментарий")),
                (
                    "stars",
                    models.CharField(
                        choices=[
                            ("⭐", "⭐"),
                            ("⭐⭐", "⭐⭐"),
                            ("⭐⭐⭐", "⭐⭐⭐"),
                            ("⭐⭐⭐⭐", "⭐⭐⭐⭐"),
                            ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
                        ],
                        default="⭐⭐⭐⭐⭐",
                        max_length=100,
                    ),
                ),
                (
                    "reviews_choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="books",
                        to="library.book",
                    ),
                ),
            ],
        ),
    ]
