# Generated by Django 4.1.2 on 2022-12-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="model_movies",
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
                ("movie", models.CharField(max_length=100)),
                ("character", models.CharField(max_length=100)),
            ],
        ),
    ]
