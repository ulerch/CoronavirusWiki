from django import template
from wiki.models import WikiEntry

register = template.Library()

@register.simple_tag
def wiki_count(r, c):
    return WikiEntry.objects.filter(row=r, column=c).count()
