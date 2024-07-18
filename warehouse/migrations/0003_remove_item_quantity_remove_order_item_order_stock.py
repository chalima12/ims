# Generated by Django 5.0.7 on 2024-07-18 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='warehouse.stock'),
            preserve_default=False,
        ),
    ]