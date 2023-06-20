from django.urls import path
from mainapp.views import index,update_data,data,updaterecord

app_name = 'mainapp'
urlpatterns = [

path('', index , name='index'),
path('data/', data , name='data'),
path('update_data/<int:calcid>/change/', update_data , name='update_data'),
path('update_data/<int:calcid>/change/updaterecord/', updaterecord, name='updaterecord'),

]
