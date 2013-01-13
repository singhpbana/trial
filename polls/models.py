from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model): 
    questions = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.questions
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice_text
    