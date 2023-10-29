# filters.py

from django import template
import re

register = template.Library()

@register.filter()
def split_sentences(value):
    # Split the input text into sentences using a regular expression
    sentences = re.split(r'(?<=[.!?])\s+', value)
    return sentences
