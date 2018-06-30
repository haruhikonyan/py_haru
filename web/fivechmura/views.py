from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Tweet

# Create your views here.
def index(request):
    tweet_list = Tweet.objects.order_by('-pub_date')

    template = loader.get_template('index.html')
    context = {
        'tweet_list': tweet_list,
    }

    return HttpResponse(template.render(context, request))

def detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    template = loader.get_template('tweet/detail.html')
    context = {
        'tweet': tweet,
    }

    return HttpResponse(template.render(context, request))

def tweet(request):
    # null の扱いがわからない
    if request.POST['owner_name'] == '':
        Tweet(tweet_text=request.POST['tweet_text'] , pub_date=timezone.now()).save()
    else:
        Tweet(owner_name=request.POST['owner_name'], tweet_text=request.POST['tweet_text'] , pub_date=timezone.now()).save()
    return HttpResponseRedirect('/')