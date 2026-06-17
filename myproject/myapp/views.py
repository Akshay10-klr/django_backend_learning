from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import features
from django.contrib.auth.models import User,auth
from django.contrib import messages

def index(request):
    features1=features.objects.all()
    return render(request, 'index.html', {'features': features1})


# Create your views here.
def counter(request):
    text=request.POST['text']
    amount_0f_words=len(text.split())
    return render(request,'cont.html',{'amount':amount_0f_words})
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email==email).exist():
                messages.info(request,'user already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'user already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                User.save();
                return redirect('login')
        else:
            messages.info(request,'invalide information')
            return redirect('register')            
    return render(request,'register.html')

