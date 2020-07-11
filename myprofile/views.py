from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from login.models import Usermaster
import os
from PIL import Image


def loadMyProfile(request):
    try:
        if request.session['session_loginRole'] == 'user':
            myProfileList = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            return render(request, 'user/profile.html', {'myProfileList': myProfileList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def insertPersonalInfo(request):
    try:
        if request.session['session_loginRole'] == 'user':
            userName = request.POST['userName']
            userMobileNo = request.POST['userMobileNo']
            userBirthdate = request.POST['userBirthdate']
            userAddress = request.POST['userAddress']
            user_LoginId = request.POST["user_LoginId"]

            if not userBirthdate:
                userBirthdate = None

            user = Usermaster.objects.get(pk=user_LoginId)
            user.userName = userName
            user.userMobileNo = userMobileNo
            user.userBirthdate = userBirthdate
            user.userAddress = userAddress
            user.save()

            return redirect('/loadMyProfile')
        else:
            return redirect('/')

    except Exception as ex:
        print(ex)


def insertSocialMediaLink(request):
    try:
        if request.session['session_loginRole'] == 'user':
            userFacebook = request.POST['userFacebook']
            userTwitter = request.POST['userTwitter']
            userInstagram = request.POST['userInstagram']
            userLinkedin = request.POST['userLinkedin']
            user_LoginId = request.POST["user_LoginId"]

            user = Usermaster.objects.get(pk=user_LoginId)
            user.userFacebook = userFacebook
            user.userTwitter = userTwitter
            user.userInstagram = userInstagram
            user.userLinkedin = userLinkedin
            user.save()

            return redirect('/loadMyProfile')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def insertNewPassword(request):
    try:
        if request.session['session_loginRole'] == 'user':
            return render(request, 'user/profile.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def insertProfilePhoto(request):
    try:
        if request.session['session_loginRole'] == 'user':
            userProfilePhoto = request.FILES['userProfilePhoto']

            if str(userProfilePhoto.name).split(".")[-1] == 'jpg' or str(userProfilePhoto.name).split(".")[
                -1] == 'png' or str(userProfilePhoto.name).split(".")[-1] == 'jpeg':

                user = Usermaster.objects.get(pk=request.session['session_Id'])
                user.userProfilePhoto = userProfilePhoto
                user.save()
                return redirect('/loadMyProfile')

            else:
                myProfileList = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
                return render(request, 'user/profile.html',
                              {'fileExtension': 'Profile photo must be .jpg, .png or .jpeg formate.',
                               'myProfileList': myProfileList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
