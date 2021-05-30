from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.
def index(request):
    return HttpResponse("this is index")


def news_view(request):
    news = News.objects.all()
    return render(request, 'news.html', {"news": news})
