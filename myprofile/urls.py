from django.urls import path

from . import views

app_name = 'myprofile'
urlpatterns = [
    path('loadMyProfile', views.loadMyProfile, name="loadMyProfile"),
    path('insertPersonalInfo', views.insertPersonalInfo, name="insertPersonalInfo"),
    path('insertSocialMediaLink', views.insertSocialMediaLink, name="insertSocialMediaLink"),
    path('insertNewPassword', views.insertNewPassword, name="insertNewPassword"),
    path('insertProfilePhoto', views.insertProfilePhoto, name="insertProfilePhoto"),

]
