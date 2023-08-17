# Generated by Django 4.1.7 on 2023-08-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_gov_my", "0046_publicationdocumentation_pub_docs_type_language_idx"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicationUpcoming",
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
                ("release_date", models.DateField()),
                ("publication_title", models.CharField(max_length=100)),
                ("product_type", models.CharField(max_length=100)),
                ("release_series", models.CharField(max_length=100)),
            ],
            options={
                "ordering": ["release_date"],
            },
        ),
        migrations.AddIndex(
            model_name="publicationupcoming",
            index=models.Index(fields=["language"], name="upcoming_pub_language_idx"),
        ),
        migrations.AddConstraint(
            model_name="publicationupcoming",
            constraint=models.UniqueConstraint(
                fields=("publication_id", "language"),
                name="unique upcoming publication by id and language",
            ),
        ),
    ]
