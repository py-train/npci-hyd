# Generated by Django 5.1.3 on 2025-03-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("acnum", models.IntegerField(primary_key=True, serialize=False)),
                ("balance", models.FloatField()),
            ],
        ),
    ]
