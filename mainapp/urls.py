from django.urls import path
from mainapp.views import index,update_data,data

app_name = 'mainapp'
urlpatterns = [

path('', index , name='index'),
path('data/', data , name='data'),
path('update_data/<int:calcid>/change/', update_data , name='update_data'),
]
