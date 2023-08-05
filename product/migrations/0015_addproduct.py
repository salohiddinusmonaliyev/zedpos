# Generated by Django 4.2.2 on 2023-07-23 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0004_rename_price_payment_payment'),
        ('product', '0014_alter_product_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField(null=True)),
                ('total_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=50)),
                ('dealer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealer.dealer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]