from django.shortcuts import render,redirect
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
        print(form)
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

    # context={'person':person_information, 'form':form}
    context={'form':form}

    return render(request,'index.html',context)


@login_required(login_url='/accounts/login')
def update_data(request,id):
    return render(request,'update_data.html')


        # def band_update(request, id):
        #     band = Band.objects.get(id=id)
        #     form = BandForm(instance=band)  # prepopulate the form with an existing band
        #     return render(request,
        #                     'listings/band_update.html',
        #                     {'form': form})

@login_required(login_url='/accounts/login')
def data(request):
    data_list=Tankcalcmetric.objects.filter(calcid__gt=465050)
    x=data_list.count()
    print(x)
    context={'data_list': data_list}
    return render(request,'data.html',context)