# Generated by Django 4.1.2 on 2023-01-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("token_api", "0002_register_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="register_user",
            name="token",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
