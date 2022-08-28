from django import template
from django.contrib.auth import get_user_model
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()

user_model = get_user_model()

@register.filter
def author_details(user, current_user=None):
  # By providing default arg it will be callable without any
  # argument
  if not isinstance(user, user_model):
    return ''
  
  if user == current_user:
    return format_html("<strong>me</strong>")

  if user.first_name and user.last_name:
    name = escape(user.first_name +" "+ user.last_name)
  else:
    name = escape(user.username)
  
  if user.email:
    # email = escape(user.email)
    # prefix = f'<a href="mailto:{email}">'
    prefix = format_html('<a href="mailto:{}">', user.email)
    sufffix = "</a>"
  else:
    prefix = ""
    sufffix = ""
  
  return mark_safe(f'{prefix}{name}{sufffix}')


