from django.db import models
import string
import secrets
from django.db import models



def urlcode():
    n=15
    while True:
        cod=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if roominfo.objects.filter(url=cod).count() == 0:
            return cod
def gencode():
    n=7
    while True:
        code=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if roominfo.objects.filter(Roomcode=code).count() == 0:
            return code

def examcode():
    n=10
    while True:
        code=''.join(secrets.choice(string.ascii_letters) for x in range(n))
        if examdetails.objects.filter(UniqCode=code).count() == 0:
            return code

#room details
class roominfo(models.Model):
    Email=models.CharField(max_length=50)
    Roomcode=models.CharField(default=gencode,max_length=7,primary_key=True)
    roomname=models.CharField(max_length=100)
    url=models.CharField(default=urlcode,max_length=15)
    roomdesc=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)



#topic specific code
class code(models.Model):
    RoomCode=models.CharField(max_length=15)
    Tpoicname=models.CharField(max_length=50)
    Tpoicdescrip=models.CharField(max_length=200)
    UniqCode=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)

#topic condent pdf
class contends(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    pdf = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200)
#temp pdf file
class tempuploader(models.Model):
    uploadfile=models.FileField(upload_to='media')
    tcode=models.CharField(max_length=20)
    def delete(self,*args, **kwargs):
        self.uploadfile.delete()
        super().delete(*args,**kwargs)
#topic condent youtube link
class youtubelink(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    link = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)

#topic condent other driev,site link
class otherlink(models.Model):
    RoomCode=models.CharField(max_length=7)
    UniqCode=models.CharField(max_length=10)
    link = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
#assiment  presntformate
class assigmentdetals(models.Model):
    assigname=models.CharField(max_length=200)
    assigdec=models.CharField(max_length=200)
    RoomCode=models.CharField(max_length=20)
    UniqCode=models.CharField(max_length=20)
    date=models.DateTimeField(auto_now_add=True)

    duedate=models.DateTimeField(max_length=200)
    totalm=models.CharField(max_length=200)





class examdetails(models.Model):
    tmail=models.CharField(max_length=50)
    UniqCode=models.CharField(max_length=10)
    examname=models.CharField(max_length=50)
    examdesc=models.CharField(max_length=200)
    examdate=models.DateTimeField(max_length=200)
    totalq=models.IntegerField()
    finish=models.BooleanField(default=False)


class examquestion(models.Model):
    UniqCode=models.CharField(max_length=10)
    qno=models.IntegerField()
    question=models.CharField(max_length=200)
    optiona=models.CharField(max_length=200)
    optionb=models.CharField(max_length=200)
    optionc=models.CharField(max_length=200)
    optiond=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)
