from django.contrib import admin
from .models import ServiceDetail
# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    readonly_fieds=('created','updated')

admin.site.register(ServiceDetail,DetailAdmin)