from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('loadChat', views.loadChat, name="loadChat"),
    path('startChat', views.startChat, name="startChat"),
    path('insertMsg', views.insertMsg, name="insertMsg"),
    path('viewChat/<int:foo>', views.viewChat, name="viewChat"),
    path('delete', views.delete, name="delete"),
    path('deleteAll', views.deleteAll, name="deleteAll"),

]
