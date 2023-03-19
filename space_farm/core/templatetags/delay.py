from django import template
import time

register = template.Library()

@register.simple_tag
def delay(seconds):
    time.sleep(seconds)