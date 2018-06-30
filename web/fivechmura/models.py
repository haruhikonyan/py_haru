from django.db import models

# Create your models here.
class Tweet(models.Model):
    owner_name = models.CharField(max_length=20, default='名無し村人')
    tweet_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return '名前:' + self.owner_name + '\n本文:\n' + self.tweet_text