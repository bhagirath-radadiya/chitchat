from django.urls import path

from . import views

app_name = 'friends'
urlpatterns = [
    path('loadFriends', views.loadFriends, name="loadFriends"),
    path('insertFriendRequest', views.insertFriendRequest, name="insertFriendRequest"),
    path('viewRequestProfile', views.viewRequestProfile, name="viewRequestProfile"),
    path('accept', views.accept, name="accept"),
    path('reject', views.reject, name="reject"),
    path('removeFriend', views.removeFriend, name="removeFriend")

]
