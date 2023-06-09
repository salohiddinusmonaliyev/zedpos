# Generated by Django 4.2.2 on 2023-06-08 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='incoming_price',
            new_name='arrival_price',
        ),
        migrations.AddField(
            model_name='product',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.measure'),
        ),
    ]
