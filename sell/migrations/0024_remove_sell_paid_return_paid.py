# Generated by Django 4.2.2 on 2023-07-15 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0023_remove_return_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='paid',
        ),
        migrations.AddField(
            model_name='return',
            name='paid',
            field=models.IntegerField(null=True),
        ),
    ]
