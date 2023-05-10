from django import template
from django.contrib.auth.decorators import login_required
from accounts.models import Person
from django.contrib.auth.models import User
from mainapp.models import Tank,Tanktype1,Tank_calibration_excel


register = template.Library()
# This tag is used for tank information for user and main page for tank exibition


@register.simple_tag(takes_context=True)
def user_tank_station(context):
    request = context['request']
    user=request.user
    # person_information=Person.objects.get(person_name=user.id)
    # user_tank=Tank.objects.filter(stationid=person_information.person_station_id)
    # user_new_tank=Tank_calibration_excel.objects.filter(station_name=person_information.person_station)
    # user_tank.append(user_new_tank)

    try:
        person_information=Person.objects.get(person_name=user.id)
        user_tank=Tank.objects.filter(stationid=person_information.person_station_id)
        if Tank_calibration_excel.objects.filter(station_name=person_information.person_station).exists():
            user_new_tank=Tank_calibration_excel.objects.filter(station_name=person_information.person_station)
        else:
            user_new_tank={'#'}

        tagcontext={'person_information':person_information,'user_tank':user_tank,'user_new_tank':user_new_tank
                    }
    except:
        user_tank="user not define"
        tagcontext={"no",}
    return tagcontext

