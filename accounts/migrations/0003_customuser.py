# Generated by Django 4.2.4 on 2023-08-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_worker_delete_customuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[("Unpaid", "Unpaid"), ("Paid", "Paid")], max_length=100
                    ),
                ),
                ("shop_name", models.CharField(max_length=200)),
            ],
        ),
    ]
