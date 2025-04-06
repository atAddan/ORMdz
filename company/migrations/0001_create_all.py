# Generated by Django 5.2 on 2025-04-03 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filial",
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
                ("name", models.CharField(max_length=44)),
                ("address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Otdel",
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
                ("name", models.CharField(max_length=255)),
                ("flor", models.CharField(max_length=255)),
                (
                    "filial",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Otdels",
                        to="company.filial",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sotr",
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
                ("full_name", models.CharField(max_length=255)),
                ("doljnost", models.CharField(max_length=255)),
                ("fone", models.CharField(blank=True, max_length=20, null=True)),
                ("data", models.DateTimeField(blank=True, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "otdel",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Sotrs",
                        to="company.otdel",
                    ),
                ),
            ],
        ),
    ]
