# Generated by Django 4.1.7 on 2023-08-07 07:47

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data_gov_my", "0038_rename_demographic_catalogjson_demography"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publication",
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
                ("publication_id", models.CharField(max_length=30)),
                (
                    "language",
                    models.CharField(
                        choices=[("en-GB", "English"), ("ms-MY", "Bahasa Melayu")],
                        default="en-GB",
                        max_length=5,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("release_date", models.DateField()),
                ("frequency", models.CharField(max_length=50)),
                (
                    "geography",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=10),
                        size=None,
                    ),
                ),
                (
                    "demography",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(blank=True, max_length=10),
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PublicationResource",
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
                ("resource_type", models.CharField(max_length=10)),
                ("resource_name", models.CharField(max_length=100)),
                ("resource_link", models.URLField(max_length=150)),
                (
                    "publication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data_gov_my.publication",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="publication",
            index=models.Index(
                fields=["publication_id", "language"],
                name="publication_id_language_idx",
            ),
        ),
        migrations.AddConstraint(
            model_name="publication",
            constraint=models.UniqueConstraint(
                fields=("publication_id", "language"),
                name="unique publication by language",
            ),
        ),
    ]
