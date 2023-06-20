from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from mainapp.forms import TankcalcmetricForm
from mainapp.models import Tankcalcmetric,Tank
from django.contrib import messages
from mainapp.calculations import natural_to_60degree_litr, cel_to_far,natural_litr
from accounts.models import Person
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login')
def index(request):

    if request.method=='POST':

        form= TankcalcmetricForm(request.POST)
        if form.is_valid():
            rdate= form.cleaned_data['rdate'].replace('/','')
            specweight=form.cleaned_data['specweight']
            temprature=form.cleaned_data['temprature']
            envtemp=form.cleaned_data['envtemp']
            tankid= form.cleaned_data['tankid']
            size= form.cleaned_data['size']
            water=int(form.cleaned_data['water'])
            naturallitr= natural_litr(tankid,size,water)
            litr60=natural_to_60degree_litr(temprature,envtemp,naturallitr,specweight)

            tankclacmetric= Tankcalcmetric(
            tankid= tankid ,
            rdate= rdate,
            billid= form.cleaned_data['billid'],
            size= size,
            temprature= temprature,
            water=water,
            status=form.cleaned_data['status'],
            specweight=specweight,
            refinery= form.cleaned_data['refinery'],
            naturallitr=naturallitr,
            litr60= litr60,
            hour= form.cleaned_data['hour'],
            cyear= rdate[0:4],
            envtemp=envtemp)

            tankclacmetric.save()
            messages.success(request, "قبوض با موفقیت ثبت شد" )
            return redirect('mainapp:index')
        else:
            messages.error(request, "قبضی ثبت نشد  " )
            return redirect('mainapp:index')
    form = TankcalcmetricForm()

    # context={'person':person_information, 'form':form}
    context={'form':form}

    return render(request,'index.html',context)


@login_required(login_url='/accounts/login')
def update_data(request,calcid):
    data_object_raw=Tankcalcmetric.objects.get(pk=calcid)
    context={'data_object_raw':data_object_raw}
    return HttpResponse(render(request,'update_data.html',context))


@login_required(login_url='/accounts/login')
def data(request):
    data_list=Tankcalcmetric.objects.filter(calcid__gt=465450)
    context={'data_list': reversed(data_list)}
    return render(request,'data.html',context)


@login_required(login_url='/accounts/login')
def updaterecord(request, calcid):
    rdate_revised= request.POST['rdate']
    specweight_revised=request.POST['specweight']
    temprature_revised=request.POST['temprature']
    envtemp_revised=request.POST['envtemp']
    tankid_revised= request.POST['tankid']
    size_revised= request.POST['size']
    water_revised=int(request.POST['water'])
    naturallitr_revised= natural_litr(tankid_revised,size_revised,water_revised)
    litr60_revised=natural_to_60degree_litr(temprature_revised,envtemp_revised,naturallitr_revised,specweight_revised)

    tankclacmetric= Tankcalcmetric(calcid=calcid)
    tankclacmetric.tankid= tankid_revised
    tankclacmetric.rdate= rdate_revised
    tankclacmetric.billid= request.POST['billid']
    tankclacmetric.size= size_revised
    tankclacmetric.temprature= temprature_revised
    tankclacmetric.water=water_revised
    tankclacmetric.status=request.POST['status']
    tankclacmetric.specweight=specweight_revised
    tankclacmetric.refinery= request.POST['refinery']
    tankclacmetric.naturallitr=naturallitr_revised
    tankclacmetric.litr60= litr60_revised
    tankclacmetric.hour= request.POST['hour']
    tankclacmetric.cyear= rdate_revised[0:4]
    tankclacmetric.envtemp=envtemp_revised
    tankclacmetric.save()
    # return HttpResponseRedirect(reverse('update_data'))
    return redirect ('update_data')

