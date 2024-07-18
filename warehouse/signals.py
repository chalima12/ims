# warehouse/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Stock

@receiver(post_save, sender=Order)
def update_stock_on_shipped(sender, instance, **kwargs):
    if instance.status == 'shipped':
        stock = instance.stock
        stock.current_level += instance.quantity
        stock.save()
