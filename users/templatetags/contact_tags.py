from django import template
from users.forms import MailingForm

register = template.Library()


@register.inclusion_tag('users/tags/mailing.html')
def mailing_form():
    return {'mailing_form': MailingForm()}
