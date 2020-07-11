from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from login.models import Usermaster, Loginmaster
from friends.models import FriendRequestmaster
from .models import Msgmaster
from datetime import datetime


# Create your views here.

def loadChat(request):
    try:
        if request.session.has_key('session_loginRole'):
            user = Usermaster.objects.filter(user_LoginId=request.session['session_Id'])
            friendList = FriendRequestmaster.objects.filter(friendRequest_From=request.session['session_Id'],
                                                            friendRequest_Action='accept')
            profilePhotoList = Usermaster.objects.all()

            return render(request, 'user/index.html', {'user': user, 'friendList': friendList,'profilePhotoList':profilePhotoList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def startChat(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_To = request.GET['friendRequest_To']
            friendRequest_From = request.GET['friendRequest_From']

            userInfo = Usermaster.objects.filter(user_LoginId=friendRequest_To)
            friendList = FriendRequestmaster.objects.filter(friendRequest_From=request.session['session_Id'],
                                                            friendRequest_Action='accept')

            chatList = Msgmaster.objects.filter(msg_To=friendRequest_To,
                                                msg_From=friendRequest_From) | Msgmaster.objects.filter(
                msg_To=friendRequest_From, msg_From=friendRequest_To)
            print(chatList, "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

            thisUser = int(request.session['session_Id'])
            thisFriend = int(friendRequest_To)
            print(thisUser, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>from>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(thisFriend, ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>to>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            profilePhotoList = Usermaster.objects.all()

            return render(request, 'user/chat.html',
                          {'friendList': friendList, 'userInfo': userInfo, 'chatList': chatList, 'thisUser': thisUser,
                           'thisFriend': thisFriend,'profilePhotoList':profilePhotoList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def insertMsg(request):
    try:
        if request.session.has_key('session_loginRole'):
            msg = request.POST['msg']
            msg_To = request.POST['msg_To']
            msg_From = request.session['session_Id']

            now = datetime.now()
            msgSendDate = now.date()
            msgSendTime = now.strftime("%I:%M:%S %p")

            chatmsg = Msgmaster(msg=msg, msg_From_id=msg_From, msg_To_id=msg_To, msgSendDate=msgSendDate,
                                msgSendTime=msgSendTime, msgSendBy=request.session['session_Id'])
            chatmsg.save()

            return redirect('/viewChat/' + msg_To)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def viewChat(request, foo):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_To = get_object_or_404(Loginmaster, pk=foo)
            friendRequest_From = request.session['session_Id']

            userInfo = Usermaster.objects.filter(user_LoginId=friendRequest_To)
            friendList = FriendRequestmaster.objects.filter(friendRequest_From=request.session['session_Id'],
                                                            friendRequest_Action='accept')

            chatList = Msgmaster.objects.filter(msg_To=friendRequest_To,
                                                msg_From=friendRequest_From) | Msgmaster.objects.filter(
                msg_To=friendRequest_From, msg_From=friendRequest_To)

            thisUser = int(request.session['session_Id'])
            thisFriend = friendRequest_To.pk
            profilePhotoList = Usermaster.objects.all()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",profilePhotoList)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", friendList)

            return render(request, 'user/chat.html',
                          {'friendList': friendList, 'userInfo': userInfo, 'chatList': chatList, 'thisUser': thisUser,
                           'thisFriend': thisFriend,'profilePhotoList':profilePhotoList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def delete(request):
    try:
        if request.session.has_key('session_loginRole'):
            id = request.GET['id']
            msg_To = request.GET['msg_To']
            # print("????????????????????????????????????????????????????????????????????????????????????????????", id, msg_To)

            deleteChat = Msgmaster.objects.get(pk=id)
            deleteChat.delete()

            return redirect('/viewChat/' + msg_To)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def deleteAll(request):
    try:
        if request.session.has_key('session_loginRole'):
            thisUser = request.GET['thisUser']
            thisFriend = request.GET['thisFriend']
            print("????????????????????????????????????????????????????????????????????????????????????????????",
                  thisUser,
                  thisFriend)

            removeAllChat = Msgmaster.objects.filter(msg_To=thisUser,
                                                     msg_From=thisFriend) | Msgmaster.objects.filter(
                msg_To=thisFriend, msg_From=thisUser)
            removeAllChat.delete()

            return redirect('/viewChat/' + thisFriend)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
