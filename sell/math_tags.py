# myapp/templatetags/math_tags.py
from django import template

register = template.Library()

@register.filter
def square(value):
    return value * value
