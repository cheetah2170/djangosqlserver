from django.db import models
from mainapp.models import REG,Station
from django.contrib.auth.models import User


class Person(models.Model):
    id=models.AutoField(primary_key=True)
    person_name=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,default=None)
    person_region=models.ForeignKey(REG,on_delete=models.DO_NOTHING,null=True,default=None)
    person_station=models.ForeignKey(Station,on_delete=models.DO_NOTHING,null=True,default=None)
    more_information=models.TextField(default=None)
   
    


