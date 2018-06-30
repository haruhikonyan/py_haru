from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tweet

# Create your views here.
def index(request):
    tweet_list = Tweet.objects.all()

    template = loader.get_template('index.html')
    context = {
        'tweet_list': tweet_list,
    }

    return HttpResponse(template.render(context, request))

def detail(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)

    template = loader.get_template('tweet/detail.html')
    context = {
        'tweet': tweet,
    }

    return HttpResponse(template.render(context, request))

def tweet(request, tweet_id):
    return HttpResponse("You're tweet %s." % tweet_id)