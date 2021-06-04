from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    air = Air.objects.all()
    corona19 = Corona19.objects.all()
    news = News.objects.all()
    weather = Weather.objects.all()
    context = {
        'air': air,
        'corona19': corona19,
        'news': news,
        'weather': weather,
    }
    
    return render(request, 'infoweb/index.html', context)
