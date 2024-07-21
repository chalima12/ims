# warehouse/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import*

@receiver(post_save, sender=Order)
def update_stock_on_order(sender, instance, **kwargs):
    if instance.status == 'shipped':
        stock = instance.stock
        stock.current_level += instance.quantity
        stock.save()


@receiver(post_save, sender=MaterialRequest)
def update_stock_on_request(sender, instance, **kwargs):
    item=instance.item
    stock = item.stock
    if instance.status == 'issued':
        
        stock.current_level -= 1
    elif instance.status == 'returned':
        stock.current_level += 1
        
    stock.save()
