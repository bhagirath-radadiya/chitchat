from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from login.models import Loginmaster, Usermaster
from .models import FriendRequestmaster, Usermaster
from chat.models import Msgmaster


# Create your views here.

def loadFriends(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest = FriendRequestmaster.objects.filter(friendRequest_To=request.session['session_Id'],
                                                               friendRequest_Action='pending')
            profilePhotoList = Usermaster.objects.all()
            return render(request, 'user/friends.html', {'friendRequest': friendRequest,'profilePhotoList':profilePhotoList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def insertFriendRequest(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_To = request.POST['friendRequest_To']
            friendRequest_From = request.session['session_Id']
            friendRequest_MSG = request.POST['friendRequest_MSG']
            friendRequest_Action = 'pending'

            friendRequest_To = Loginmaster.objects.filter(loginUserName=friendRequest_To)
            if len(friendRequest_To) != 0:
                friendRequest_To = friendRequest_To[0].id

                r1 = FriendRequestmaster.objects.filter(friendRequest_To_id=friendRequest_To,
                                                        friendRequest_From_id=friendRequest_From,
                                                        friendRequest_Action='accept').exists()
                r2 = FriendRequestmaster.objects.filter(friendRequest_To_id=friendRequest_From,
                                                        friendRequest_From_id=friendRequest_To,
                                                        friendRequest_Action='accept').exists()
                r3 = FriendRequestmaster.objects.filter(friendRequest_To_id=friendRequest_To,
                                                        friendRequest_From_id=friendRequest_From,
                                                        friendRequest_Action='pending').exists()
                r4 = FriendRequestmaster.objects.filter(friendRequest_To_id=friendRequest_From,
                                                        friendRequest_From_id=friendRequest_To,
                                                        friendRequest_Action='pending').exists()

                if r1 == False:
                    if r3 == True:
                        friendRequest = FriendRequestmaster.objects.filter(
                            friendRequest_To=request.session['session_Id'],
                            friendRequest_Action='pending')
                        return render(request, 'user/friends.html',
                                      {'requestPending': 'you request in pening.', 'friendRequest': friendRequest})
                    if r4 == True:
                        friendRequest = FriendRequestmaster.objects.filter(
                            friendRequest_To=request.session['session_Id'],
                            friendRequest_Action='pending')
                        return render(request, 'user/friends.html',
                                      {'showRequest': 'Request already send to you', 'friendRequest': friendRequest})


                    elif r2 == False:
                        friendRequest = FriendRequestmaster(friendRequest_To_id=friendRequest_To,
                                                            friendRequest_From_id=friendRequest_From,
                                                            friendRequest_MSG=friendRequest_MSG,
                                                            friendRequest_Action=friendRequest_Action)
                        friendRequest.save()
                        return redirect('/loadFriends')
                    elif r2 == True:
                        friendRequest = FriendRequestmaster.objects.filter(
                            friendRequest_To=request.session['session_Id'],
                            friendRequest_Action='pending')
                        return render(request, 'user/friends.html',
                                      {'alreadyFriend': 'you both are already friends.',
                                       'friendRequest': friendRequest})



                else:
                    friendRequest = FriendRequestmaster.objects.filter(friendRequest_To=request.session['session_Id'],
                                                                       friendRequest_Action='pending')
                    return render(request, 'user/friends.html',
                                  {'alreadyFriend': 'you both are already friends.', 'friendRequest': friendRequest})
            else:
                friendRequest = FriendRequestmaster.objects.filter(friendRequest_To=request.session['session_Id'],
                                                                   friendRequest_Action='pending')
                return render(request, 'user/friends.html',
                              {'userNotFound': 'This User is not Available.', 'friendRequest': friendRequest})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def viewRequestProfile(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_To = request.GET['friendRequest_To']
            userProfile = Usermaster.objects.filter(user_LoginId=friendRequest_To)

            friendRequest = FriendRequestmaster.objects.filter(
                friendRequest_To=request.session['session_Id'], friendRequest_Action='pending')
            profilePhotoList = Usermaster.objects.all()

            return render(request, 'user/friends.html', {'userProfile': userProfile, 'friendRequest': friendRequest,'profilePhotoList':profilePhotoList})
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def accept(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_From = request.GET['friendRequest_From']

            friendRequest = FriendRequestmaster.objects.get(friendRequest_From_id=friendRequest_From,
                                                            friendRequest_To_id=request.session['session_Id'])
            friendRequest.friendRequest_Action = 'accept'
            friendRequest.save()
            duplicate = FriendRequestmaster(friendRequest_To_id=friendRequest_From,
                                            friendRequest_From_id=request.session['session_Id'],
                                            friendRequest_Action='accept')
            duplicate.save()

            return redirect('/loadFriends')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def reject(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_From = request.GET['friendRequest_From']
            friendRequest = FriendRequestmaster.objects.get(friendRequest_From_id=friendRequest_From,
                                                            friendRequest_To_id=request.session['session_Id'])
            friendRequest.delete()

            return redirect('/loadFriends')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


def removeFriend(request):
    try:
        if request.session.has_key('session_loginRole'):
            friendRequest_From = request.GET['thisUser']
            friendRequest_To = request.GET['thisFriend']

            removeFriendList = FriendRequestmaster.objects.filter(friendRequest_From=friendRequest_From,
                                                                  friendRequest_To=friendRequest_To) | FriendRequestmaster.objects.filter(
                friendRequest_To=friendRequest_From, friendRequest_From=friendRequest_To)
            removeFriendList.delete()

            removeAllChat = Msgmaster.objects.filter(msg_To_id=friendRequest_To,
                                                     msg_From_id=friendRequest_From) | Msgmaster.objects.filter(
                msg_To_id=friendRequest_From, msg_From_id=friendRequest_To)
            removeAllChat.delete()

            return redirect('/loadChat')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
