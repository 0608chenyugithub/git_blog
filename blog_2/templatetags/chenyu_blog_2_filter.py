from django import template
register=template.Library()


@register.filter(name='cutLeft')
def cutLeft(value, arg):
    """Removes all values of arg from the given string"""
    return value.split(arg)[0]


@register.filter(name='cutRight')
def cutRight(value, arg):
    """Removes all values of arg from the given string"""
    return value.split(arg)[1]