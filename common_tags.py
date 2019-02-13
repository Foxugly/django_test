from django import template
import re
register = template.Library()


@register.filter(name='hash')
def hash(h, key):
	return h[key]


@register.filter(name='verbose_name')
def verbose_name(obj):
    return obj._meta.verbose_name	