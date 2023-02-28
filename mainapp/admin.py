from django.contrib import admin

from mainapp.models import Tankcalcmetric, Station, Tank

  
class TankcalcmetricAdmin(admin.ModelAdmin):
    list_display = ('tankid', 'rdate', 'billid','status', 'litr60')
    list_per_page = 200
    search_fields=['tankid', 'rdate', 'billid']
    
    
  
admin.site.register(Tankcalcmetric,TankcalcmetricAdmin)
admin.site.register(Station)
admin.site.register(Tank)