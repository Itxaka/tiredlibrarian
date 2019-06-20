from django import template
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import title


register = template.Library()


@register.inclusion_tag('nav-item.html', takes_context=True, name="navitem")
def navitem(context, text):
    """Takes text and generates the navbar entry for it"""
    request = context.get('request')
    active = True if text in request.path else False

    return {
        "active": active,
        "text": title(text),
        "url": reverse(text)
    }


@register.simple_tag
def version():
    """Return version from the settings"""
    return getattr(settings, "VERSION", "")
