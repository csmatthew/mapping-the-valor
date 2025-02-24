from django import template

register = template.Library()


@register.filter
def url_name(obj):
    return obj.get_url_name()
