from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WeChatUser(models.Model):
    user =  models.OneToOneField(User)
    motoo = models.CharField(max_length=100,null=True,blank =True)
    pic=models.CharField(max_length=80,null=True,blank=True)
    regions=models.CharField(max_length=50,null=True,blank=True)
    def __unicode__(self):
        return self.user.username


class Status(models.Model):
    user=models.ForeignKey(WeChatUser)
    text = models.CharField(max_length=140)
    pic = models.CharField(max_length=80,null=True,blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return  self.text

class Meta:
    ordering =['id']



