# Generated by Django 4.2.2 on 2023-06-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('ph_number', models.CharField(max_length=50, verbose_name='Phone number')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]