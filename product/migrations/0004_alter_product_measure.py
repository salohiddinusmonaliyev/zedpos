# Generated by Django 4.2.1 on 2023-05-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='measure',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
