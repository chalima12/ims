# Generated by Django 5.0.7 on 2024-07-18 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_remove_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
