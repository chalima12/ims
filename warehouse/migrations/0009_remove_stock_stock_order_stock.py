# Generated by Django 5.0.7 on 2024-07-18 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_remove_order_stock_stock_stock_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='stock',
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='warehouse.stock'),
            preserve_default=False,
        ),
    ]
