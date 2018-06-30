from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /tweet/5/
    path('tweet/<int:tweet_id>/', views.detail, name='detail'),
]