from django.template import Library
from thumbnail import athumbnail

register = Library()

register.tag(athumbnail)
