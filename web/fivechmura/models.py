from django.db import models

# Create your models here.
class Tweet(models.Model):
    owner_name = models.CharField(max_length=20)
    tweet_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return 'name:' + self.owner_name + 'tweet:' + self.tweet_text