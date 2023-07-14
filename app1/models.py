
from django.db import models
from ntpath import join
from django.contrib.auth.models import User

class userlogin(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image/", null=True)
    email=models.CharField(max_length=255)
    
# Create your models here.
class post(models.Model):
    user = models.ForeignKey(userlogin, on_delete=models.CASCADE, null=True)
    description=models.TextField()
    tag = models.CharField(max_length=50, null=True)
    like = models.IntegerField(null=True,default=0)
    dislike = models.IntegerField(null=True,default=0)
    head = models.CharField(max_length=255, null=True)

