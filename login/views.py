from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from .models import Loginmaster, Usermaster

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.base_user import BaseUserManager


# Create your views here.

def custom_page_not_found_view(request, exception):
    return render(request, "user/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "user/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "user/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "user/400.html", {})


def loadLogin(request):
    request.session.clear()
    return render(request, 'user/signin.html')


def insertLogin(request):
    loginUserName = request.POST['userName']
    loginPassword = request.POST['password']


    loginList = Loginmaster.objects.filter(loginUserName=loginUserName, loginPassword=loginPassword)  # validation
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",loginList,loginUserName,loginPassword)

    loginDictList = [i.__dict__ for i in loginList]  # convert object to dictionary

    if len(loginDictList) == 0:
        return render(request, 'user/signin.html', {'userNotExist': 'Username Or Password is Incorrect !'})
    else:
        for row in loginDictList:
            request.session['session_Id'] = row['id']
            request.session['session_loginUserName'] = row['loginUserName']
            request.session['session_loginRole'] = row['loginRole']

        return redirect('/loadChat')


def loadRegister(request):
    return render(request, 'user/signup.html')


def insertRegister(request):
    userName = request.POST['name']
    loginUserName = request.POST['userName']
    loginRole = 'user'

    loginPassword = str(BaseUserManager().make_random_password(8))

    print("loginPassword=" + loginPassword)

    sender = "p2ploans2020@gmail.com"

    receiver = loginUserName

    msg = MIMEMultipart()

    msg['From'] = sender

    msg['To'] = receiver

    msg['Subject'] = "ChitChat Password"

    msg.attach(MIMEText(loginPassword, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender, "finelyear2020")

    text = msg.as_string()

    server.sendmail(sender, receiver, text)

    if Loginmaster.objects.filter(loginUserName=loginUserName, loginRole=loginRole).exists() == False:
        register = Loginmaster(loginUserName=loginUserName, loginPassword=loginPassword,
                               loginRole=loginRole)  # insert
        register.save()

        user = Usermaster(userName=userName, user_LoginId=register)
        user.save()

        return render(request, 'user/signin.html')

    else:
        msg = 'This username is already Exist.'
        return render(request, 'user/signup.html', {'msg': msg})


def updatePassword(request):
    try:
        if request.session.has_key('session_loginRole'):
            currentPassword = request.POST['currentPassword']
            newPassword = request.POST['newPassword']
            conformPassword = request.POST['conformPassword']

            validation = Loginmaster.objects.get(pk=request.session['session_Id'])

            if currentPassword != validation.loginPassword:
                myProfileList = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
                oldPasswordError = 'Current Password is not match with Old Password.'
                return render(request, 'user/profile.html',
                              {'myProfileList': myProfileList, 'oldPasswordError': oldPasswordError})

            elif newPassword != conformPassword:
                myProfileList = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
                noMatch = 'new password and conform password is not match.'
                return render(request, 'user/profile.html', {'myProfileList': myProfileList, 'noMatch': noMatch})

            elif validation.pk == request.session['session_Id']:
                validation.loginPassword = newPassword
                validation.save()

                myProfileList = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
                successfully = 'Password change successfully.'
                return render(request, 'user/profile.html',
                              {'myProfileList': myProfileList, 'successfully': successfully})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def forgotPassword(request):
    return render(request, 'user/forgotPassword.html')


def insertForgotPassword(request):
    loginUserName = request.POST['loginUserName']

    validation = Loginmaster.objects.filter(loginUserName=loginUserName).exists()

    if validation == True:
        password = Loginmaster.objects.get(loginUserName=loginUserName)

        sender = "p2ploans2020@gmail.com"

        receiver = loginUserName

        msg = MIMEMultipart()

        msg['From'] = sender

        msg['To'] = receiver

        msg['Subject'] = "Forgot Password"

        msg.attach(MIMEText(password.loginPassword, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender, "finelyear2020")

        text = msg.as_string()

        server.sendmail(sender, receiver, text)

        return render(request, 'user/signin.html')

    else:

        return render(request, 'user/forgotPassword.html', {'userNotExist': 'This User is not Registered'})
