from django.template import Library
from athumbnail import athumbnail

register = Library()

register.tag(athumbnail)
