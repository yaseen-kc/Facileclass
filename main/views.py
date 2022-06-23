from lib2to3.pgen2 import token
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages 
from django.contrib.messages.api import error
from django.views.decorators.csrf import csrf_protect
from .mailsender import *

# Create your views here.
@csrf_protect
def home(request):
    if request.session._session:
        return redirect('/login')
    return render(request,"index.html")


def login(response):
    if response.session._session:
        try:
            email = response.session['mail']
            if admin_info.objects.filter(Email=email):
                return redirect('/adminl/')
            elif teacher_info.objects.filter(Email=email):
                return redirect('/teachl/')
            elif user_info.objects.filter(Email=email):
                return redirect('/studl/')
        except KeyError:
            pass
    if response.method == 'POST':
        if response.POST.get("signin"):
            email = response.POST.get("UL_email")
            password = response.POST.get("UL_pass")
            if admin_info.objects.filter(Email = email).exists():
                to = admin_info.objects.get(Email=email)
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/adminl/')
                else:
                    messages.error(response,'Password incorrect')
                    return redirect('/')
            elif teacher_info.objects.filter(Email=email).exists():
                to = teacher_info.objects.get(Email=email)
                if to.Activate == False:
                    messages.error(response,'Account is not Activated')
                    return redirect('/')
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/teachl/')
                else:
                    messages.error(response,'Password Incorrect')
                    return redirect('/')
            elif user_info.objects.filter(Email=email).exists():
                to = user_info.objects.get(Email=email)
                if to.passwords == password:
                    response.session['mail'] = email
                    return redirect('/studl/')
                else:
                    messages.error(response,'Password incorrect')
            else:
                messages.error(response,'Email not found')
                return redirect('/')
    return render(response,"index.html")
def activation(request,tk):
    print(tk[-6:])
    if tk[-6:] == 'forget':
        if user_info.objects.filter(token=tk[:-6]).exists():
            request.session['mail'] = teacher_info.objects.get(token=tk[:-6]).Email
        elif teacher_info.objects.filter(token=tk[:-6]).exists():
            request.session['mail'] = teacher_info.objects.get(token=tk[:-6]).Email
            return render(request,"fpass.html")
        else:
            return redirect('/')
    if teacher_info.objects.filter(token=tk).exists():
        request.session['mail'] = teacher_info.objects.get(token=tk).Email
        return render(request,"mailvar.html")
    if user_info.objects.filter(token=tk).exists():
        request.session['mail'] = user_info.objects.get(token=tk).Email
        return render(request,"mailvar.html")
    return redirect('/')
def forgetpassmailsend(request):
    if request.method == "POST":
        if request.POST.get("passmail"):

            mail = request.POST.get("U_email")
            print(mail)
            if not admin_info.objects.filter(Email=mail).exists():
                if not teacher_info.objects.filter(Email=mail).exists():
                    if not user_info.objects.filter(Email=mail).exists():
                        messages.error("Email Does not exist")
                        return redirect('/')
                    else:
                        tk = user_info.objects.get(Email=mail).token
                        subject = "Password Reset Link"
                        text = "Follow the link to change your password\n"
                        message = 'Subject: {}\n\n{}'.format(subject,text)
                        mailsender(tk+"forget",mail,message)
                        messages.success(request,"Mail sented successfully")
                        return redirect('/')
                else:
                        tk = teacher_info.objects.get(Email=mail).token
                        print(tk)
                        subject = "Password Reset Link"
                        text = "Follow the link to change your password\n"
                        message = 'Subject: {}\n\n{}'.format(subject,text)
                        mailsender(tk+"forget",mail,message)
                        messages.success(request,"Mail sented successfully")
                        return redirect('/')
            else:
                messages.error("contact developer")
    return redirect('/')

def activatea(request):
    email = request.session['mail']
    if request.method == 'POST':
        name = request.POST.get("U_name1")
        passwrd = request.POST.get("U_password1")
        if user_info.objects.filter(Email=email).exists():
            user_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('studl/')
        elif teacher_info.objects.filter(Email=email).exists():
            teacher_info.objects.filter(Email=email).update(Activate=True,passwords=passwrd,Name=name)
            messages.error(request, 'Your acount is Activated')
            request.session['mail'] = email
            return redirect('teachl/')
        else:
            messages.error(request, 'Email not found Contact Admin')
            return redirect('/')
    
        

def newpass(request):
    email = request.session['mail']
    if request.method == 'POST':
        passwrd = request.POST.get("U_password1")
        if user_info.objects.filter(Email=email).exists():
            user_info.objects.filter(Email=email).update(passwords=passwrd)
            messages.error(request, 'New Password is set')
            request.session['mail'] = email
            return redirect('/')
        elif teacher_info.objects.filter(Email=email).exists():
            teacher_info.objects.filter(Email=email).update(passwords=passwrd)
            messages.error(request, 'New Password is set')
            request.session['mail'] = email
            return redirect('/')
        else:
            messages.error(request, 'Email not found Contact Admin')
            return redirect('/')
    