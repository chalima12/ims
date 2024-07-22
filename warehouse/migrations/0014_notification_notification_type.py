# Generated by Django 5.0.7 on 2024-07-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0013_notification_read_alter_materialrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('User', 'User'), ('Category', 'Category'), ('Stock', 'Stock'), ('Item', 'Item'), ('Order', 'Order'), ('MaterialRequest', 'MaterialRequest')], default='MaterialRequest', max_length=50),
        ),
    ]