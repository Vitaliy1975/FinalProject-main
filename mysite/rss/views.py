from django.shortcuts import render
from .models import News
from .tasks import  news_rss

# Create your views here.
def rss(request):
    scrap=news_rss()
    articles=News.objects.all()
    return render(request,"rss/home.html",{"articles":articles})
