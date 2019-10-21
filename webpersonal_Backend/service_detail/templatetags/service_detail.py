from django import template
from service_detail.models import ServiceDetail

register=template.Library()

@register.simple_tag
def get_service_detail_list():
    detail = ServiceDetail.objects.all()
    return detail