# Generated by Django 5.1.3 on 2025-03-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=10
                    ),
                ),
            ],
        ),
    ]
