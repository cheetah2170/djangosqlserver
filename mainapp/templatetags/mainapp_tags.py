from django import template
from django.contrib.auth.decorators import login_required
from accounts.models import Person
from django.contrib.auth.models import User
from mainapp.models import Tank,Tanktype1

register = template.Library()
# This tag is used for tank information for user and main page
@register.simple_tag(takes_context=True)
def user_tank_station(context):
    request = context['request']
    user=request.user
    try:
        person_information=Person.objects.get(person_name=user.id)
        user_tank=Tank.objects.filter(stationid=person_information.person_station_id)
        tagcontext={'person_information':person_information,'user_tank':user_tank}
    except:
        user_tank="user not define"
    return tagcontext

