import markdown as md
from django import template
from django.template.defaultfilters import stringfilter



register = template.Library()


@register.filter()
def convert_markdown(value):
    return md.markdown(value)

