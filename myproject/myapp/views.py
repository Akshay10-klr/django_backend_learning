from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import features

def index(request):
    features1=features.objects.all()
    return render(request, 'index.html', {'features': features1})


# Create your views here.
def counter(request):
    text=request.POST['text']
    amount_0f_words=len(text.split())
    return render(request,'cont.html',{'amount':amount_0f_words})