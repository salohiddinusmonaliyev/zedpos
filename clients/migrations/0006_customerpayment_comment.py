# Generated by Django 4.2.2 on 2023-06-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_customerpayment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpayment',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
