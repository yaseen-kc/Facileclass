from enum import unique
from django.db import models

# Create your models here.


class sroominfo(models.Model):
    Email=models.CharField(max_length=50)
    Roomcode=models.CharField(max_length=7)
    roomname=models.CharField(max_length=100)
    url=models.CharField(max_length=15)
    roomdesc=models.CharField(max_length=200)


class assigmnet(models.Model):
    RoomCode=models.CharField(max_length=20)
    UniqCode=models.CharField(max_length=10)
    pdf = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200)
    mark=models.CharField(max_length=200)
    totalm=models.CharField(max_length=200)

class stexamdetails(models.Model):
    unique=models.CharField(max_length=7)
    stmail=models.CharField(max_length=10)
    stname=models.CharField(max_length=100)
    score=models.CharField(max_length=200)
    finshed=models.CharField(max_length=200)
