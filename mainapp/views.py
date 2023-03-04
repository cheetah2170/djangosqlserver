from django.shortcuts import render,redirect
# from django.http import HttpResponse
from mainapp.forms import TankcalcmetricForm
from mainapp.models import Tankcalcmetric
from django.contrib import messages 
from mainapp.calculations import natural_to_60degree_litr, cel_to_far,natural_litr


def index(request):
    if request.method=='POST':
    
        form= TankcalcmetricForm(request.POST)
        if form.is_valid():
            rdate= form.cleaned_data['rdate'].replace('-','')
            specweight=form.cleaned_data['specweight']
            temprature=cel_to_far(form.cleaned_data['temprature'])
            envtemp=cel_to_far(form.cleaned_data['envtemp'])
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
            cyear= rdate[2:4],
            envtemp=envtemp)

            tankclacmetric.save()
            messages.success(request, "قبوض با موفقیت ثبت شد" )
            return redirect('mainapp:index')
        else:
            messages.error(request, "قبضی ثبت نشد  " )
            return redirect('mainapp:index')
    form = TankcalcmetricForm()
    return render(request,'index.html',{'form':form})