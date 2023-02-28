from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def  login_view(request):
    if request.method == "POST":
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "نام کابری یا رمز عبور اشتباه است" )
            return render(request,'login.html')
        

    else:
        return render(request,'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')