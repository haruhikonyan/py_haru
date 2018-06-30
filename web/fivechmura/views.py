from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, 5channeler ここにtwitterみたいなのを作ろうと思う")

def detail(request, tweet_id):
    return HttpResponse("You're looking at tweet %s." % tweet_id)

def tweet(request, tweet_id):
    return HttpResponse("You're tweet %s." % tweet_id)