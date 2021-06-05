from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime
from pytz import timezone

# Create your views here.
def index(request):
    today = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    print(today)
    air = Air.objects.filter(datatime__contains=today)
    print('[+]air: ',air)
    corona19 = Corona19.objects.filter(createdt__contains=today)
    print('[+]corona19: ',corona19)
    news = News.objects.all()
    weather = Weather.objects.filter(basedate__contains=today)
    print('[+]weather: ', weather)
    context = {
        'air': air,
        'corona19': corona19,
        'news': news,
        'weather': weather,
    }
    
    return render(request, 'infoweb/index.html', context)
