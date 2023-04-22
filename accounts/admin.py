from django.contrib import admin
from accounts.models import Person
from django.contrib.auth.models import User



class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_name','can_change_data','person_fullname')
    
    def person_fullname(self,obj):
        person_fisrtname=User.objects.get(username=obj.person_name).first_name
        person_lastname=User.objects.get(username=obj.person_name).last_name
        person_fullname=person_fisrtname +" "+ person_lastname
        return person_fullname
    
admin.site.register(Person,PersonAdmin)


