# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='gt')
def greater_than(value, arg):
    return value > arg
