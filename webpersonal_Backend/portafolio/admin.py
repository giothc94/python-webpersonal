from django.contrib import admin
from .models import Portafolio
# Register your models here.
class PortafolioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Portafolio,PortafolioAdmin)
