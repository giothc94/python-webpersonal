from django.shortcuts import render, get_object_or_404
from .models import ServiceDetail

# Create your views here.
def detail(request,detail_id):
    detail = get_object_or_404(ServiceDetail,id=detail_id)
    return render(request,"service_detail/detail.html",{'detail':detail})