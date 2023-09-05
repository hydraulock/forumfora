from django import template
from django.utils.timesince import timesince
from django.utils.translation import gettext as _
from datetime import timedelta
from django.utils import timezone

register = template.Library()


@register.filter
def simplified_timesince(value):
    """
    Returns a simplified string representing time difference in days, months, or years.
    """
    now = timezone.now()
    diff = now - value

    if diff < timedelta(days=30):
        days = diff.days
        if days == 0:
            return _("Aujourd'hui")
        elif days == 1:
            return _("Hier")
        else:
            return _("Il y a %d jours") % days
    elif diff < timedelta(days=365):
        months = diff.days // 30
        if months == 1:
            return _("Il y a 1 mois")
        else:
            return _("I y a %d mois") % months
    else:
        years = diff.days // 365
        if years == 1:
            return _("Il y a 1 an")
        else:
            return _("Il y a %d ans") % years
