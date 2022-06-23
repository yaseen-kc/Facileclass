from main.models import user_info
from teachl.models import *
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.api import error
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json
from django.contrib import messages


gauth=GoogleAuth()

global popupurl
popupurl='0'
def userp(response):
    email = response.session['mail']
    ls = sroominfo.objects.filter(Email=email)
    context = {
        'ls':ls
    }
    return render(response,"upage.html",{'context':context})
    

    
def logout(response):
    response.session.flush()
    return HttpResponseRedirect('/')
    
def createclass_form(request):
    return render(request,"addpage.html")


def createclass(request):
    mail = request.session['mail']
    if request.method == 'POST':
        if request.POST.get('add'):
            classname = request.POST.get('clsname')
            if roominfo.objects.filter(Roomcode=classname).exists():
                ls=roominfo.objects.get(Roomcode=classname)
                to = sroominfo(Email=mail,Roomcode=ls.Roomcode,roomname=ls.roomname,url=ls.url,roomdesc=ls.roomdesc)
                to.save()
            else:
                messages.error(request,'Incorrept code')
        
            return redirect('/')
        return redirect('/')
    return redirect('/')



def classwork(requset,cod):
     tk = requset.session['mail']
     if user_info.objects.filter(Email=tk).exists():
          if roominfo.objects.filter(url=cod).exists():
               presnt=datetime.now()
               
               rcod=roominfo.objects.get(url=cod)
               print('\n',rcod.Roomcode,'\n')
               if not popupurl== '0':
                    context={
                         'url':cod,
                         'rcode':rcod,
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod),
                         "presntformate":presnt,
                         "upload":assigmnet.objects.filter(RoomCode=cod),
                         "assment":assigmentdetals.objects.filter(RoomCode=cod),
                         "popuplink":popupurl
                         }
               else:
                    context={
                         'url':cod,
                         'rcode':rcod,
                         "pdf":contends.objects.filter(RoomCode=cod),
                         "ls":code.objects.filter(RoomCode=cod),
                         "presntformate":presnt,
                         "yt":youtubelink.objects.filter(RoomCode=cod),
                         "upload":assigmnet.objects.filter(RoomCode=cod),
                         "assment":assigmentdetals.objects.filter(RoomCode=cod),
                         "link":otherlink.objects.filter(RoomCode=cod)
                         }
               return render(requset, "sclasswork.html",{'context':context})

def prople(requset,cod):
     tk = requset.session['mail']
     print('\nhi\n')
     print('\n',tk,'\n')
     if user_info.objects.filter(Email=tk).exists():
          if roominfo.objects.filter(url=cod).exists():
               
               rcod=roominfo.objects.get(url=cod)
               print(sroominfo.objects.filter(Roomcode=cod))
               context={
                         'url':cod,
                         'rcode':rcod,
                         'tk':tk,
                         "teacher":roominfo.objects.filter(Roomcode=rcod.Roomcode)[0],
                         "student":sroominfo.objects.filter(Roomcode=rcod.Roomcode),


                         }
               return render(requset, "speople.html",{'context':context})




def uploader(respnce,cod,tcod):
     if respnce.method == 'POST':
          duedate=assigmentdetals.objects.get(UniqCode=tcod).duedate
          present=datetime.now()
         
          GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = 'client_secrets.json'
          if respnce.POST.get('pdfupload'):
               print("heelo")
               pdffiles=respnce.FILES.getlist('pdffiles') #multi pdf upload
               print(pdffiles)

               dpdf=tempuploader.objects.all()
               for pd in dpdf:
                    pd.delete()
               for f in pdffiles: 

                    drivepassway=tempuploader(uploadfile=f,tcode=tcod) #storing the multiple pdf in temp uploader
                    drivepassway.save()
          try:
               print("try")
               gauth.LoadCredentialsFile("creds.json")
               if gauth.credentials is None:
                    return HttpResponseRedirect(gauth.GetAuthUrl())
               elif gauth.access_token_expired:
                    print("refresh")
                    gauth.Refresh()
               else:
                    print(gauth.credentials)
                    gauth.Authorize()
                    print("success")
               
               gauth.SaveCredentialsFile("creds.json")
               drive=GoogleDrive(gauth)
               pdffile=tempuploader.objects.all()
               for f in pdffile:
                    print("hi")
                    ls=assigmnet.objects.get(UniqCode=f.tcode) #tcode=topic code (Unique code  a identify the topic)
                    parernt_id=folderspcifing(ls,drive)
                    pathfile= f.uploadfile.path
                    gfile = drive.CreateFile({'parents': [{'id': parernt_id}]})
                    gfile.SetContentFile(pathfile)
                    print("hi2")
                    gfile.Upload()
                    print("updone")
                    con=assigmnet(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,pdf=gfile.get('id'),name=user_info.objects.get(Email=respnce.session['mail']).Name,totalm="20",mark="none") #drive file  id storing
                    con.save()

               return redirect('/studl/c/'+cod)
          except FileNotFoundError:
               global popupurl
               popupurl= gauth.GetAuthUrl()
               return HttpResponseRedirect(gauth.GetAuthUrl())
             






def Gauthcheck(respnce):
     url=gauth.GetAuthUrl()
     print(url)
     return url


def callback(request): 
     if request.method == 'GET':
        cod = request.GET.get('code')
        if cod == None:
          return render(request,'scallback.html')
        gauth.Auth(cod)
        gauth.SaveCredentialsFile('creds.json')
        drive = GoogleDrive(gauth) 
        global urladder
        pdffiles=tempuploader.objects.all() #geting all temp uploaded file
        for f in pdffiles:
          ls=assigmentdetals.objects.get(UniqCode=f.tcode) #assimentcodes=assimentcodes code (Unique code  a identify the assimentcodes)
          parernt_id=folderspcifing(ls,drive)
          urladder=ls.RoomCode
          pathfile= f.uploadfile.path
          print('\n'+f.uploadfile.path+'\n')
          gfile = drive.CreateFile({'parents': [{'id': parernt_id}]})
          gfile.SetContentFile(pathfile)
          gfile.Upload()
          gfile.InsertPermission({
                  'role':'reader',
                  'type':'anyone'
             })
          con=assigmnet(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,pdf=gfile.get('id'),name=user_info.objects.get(Email=request.session['mail']).Name,totalm="20",mark="none") #drive file  id storing
          con.save()      
        reurl='/studl/c/'+urladder
        return redirect(reurl)
     return render(request,"scallback.html")

     

def folderspcifing(ls,drive):
    foder_title="WEBCLASSROOM"
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folder_id=None
    folder_id_in=None
    for file in file_list:
        if(file['title']==foder_title):
            folder_id=file['id']
            break
    if folder_id==None:
        folder_id=createmainfolder(drive)
    children = drive.ListFile({'q': "'" + folder_id + "' in parents"}).GetList()
    for file in children:    
        if(file['title']==ls.RoomCode):
            folder_id_in=file['id']
            break
    if folder_id_in==None:
        folder_id_in=classroomfolder(ls,folder_id,drive)
    return folder_id_in
    

def createmainfolder(drive):
    folder_name="WEBCLASSROOM"
    folder=drive.CreateFile({'title':folder_name,'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')

def classroomfolder(ls,folder_id,drive):
    folder_name=ls.RoomCode
    folder=drive.CreateFile({'title':folder_name,'parents' :  [{"id": folder_id, "kind": "drive#childList"}],'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')
