# Generated by Django 4.2.4 on 2023-08-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
