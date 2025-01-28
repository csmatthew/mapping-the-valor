from django import template
from ..models import FinancialDetail

register = template.Library()

@register.filter
def calculate_grand_total_lsd(details):
    return FinancialDetail.calculate_grand_total_lsd(details)