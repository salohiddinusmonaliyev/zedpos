# Generated by Django 4.2.1 on 2023-06-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_remove_dealeroutput_worker'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DealerOutput',
            new_name='Payment',
        ),
    ]