from django import template

register = template.Library()

@register.filter()
def preview_url(path):
    if path:
        return f'/media/{path}'
    return '#'