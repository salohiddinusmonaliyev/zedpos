# Generated by Django 4.2.2 on 2023-07-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_customerpayment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpayment',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]