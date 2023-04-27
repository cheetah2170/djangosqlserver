from django.contrib import admin

from mainapp.models import Tankcalcmetric, Station, Tank, Regidentification,Station_Region_Relation,REG,Tank_calibration_excel
from mainapp.models import Oilproducts,Tanktype1

  
class TankcalcmetricAdmin(admin.ModelAdmin):
    list_display = ('tankid', 'rdate', 'billid','status', 'litr60')
    list_per_page = 200
    search_fields=['tankid', 'rdate', 'billid']
    
class Station_Region_RelationAdmin(admin.ModelAdmin):
    list_display=('regname','stationname')

class TankAdmin(admin.ModelAdmin):
    list_display = ('tankid', 'tankname', 'stationid','prodid', 'tanktype','station_name')
    search_fields=['tankid', 'prodid']    
    def station_name(self,obj):
        station_name=Station.objects.get(stationid=obj.stationid).stationname
        return station_name

admin.site.register(Tankcalcmetric,TankcalcmetricAdmin)
admin.site.register(Station)
admin.site.register(Tank,TankAdmin)
admin.site.register(Regidentification)
admin.site.register(REG)
admin.site.register(Oilproducts)
admin.site.register(Tank_calibration_excel)
admin.site.register(Station_Region_Relation,Station_Region_RelationAdmin)
