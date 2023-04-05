# Generated by Django 4.1 on 2023-02-19 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partygame", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category2",
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
                ("title", models.CharField(max_length=20, verbose_name="カテゴリ")),
            ],
        ),
        migrations.CreateModel(
            name="Category3",
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
                ("title", models.CharField(max_length=20, verbose_name="カテゴリ")),
            ],
        ),
        migrations.CreateModel(
            name="Category4",
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
                ("title", models.CharField(max_length=20, verbose_name="カテゴリ")),
            ],
        ),
    ]