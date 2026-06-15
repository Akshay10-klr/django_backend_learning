from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import*

def index(request):
    feature1=features()
    feature1.name='fast'
    feature1.id=0
    feature1.details='its very fast'

    feature2=features()
    feature2.name='fast'
    feature2.id=1
    feature2.details='its very fast'

    feature3=features()
    feature3.name='fast'
    feature3.id=2
    feature3.details='its very fast'

    feature4=features()
    feature4.name='fast'
    feature4.id=3
    feature4.details='its very fast'
    features_list = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features': features_list})


# Create your views here.
def counter(request):
    text=request.POST['text']
    amount_0f_words=len(text.split())
    return render(request,'cont.html',{'amount':amount_0f_words})