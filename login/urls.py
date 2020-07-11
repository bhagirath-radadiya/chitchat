from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.loadLogin, name='loadLogin'),
    path('insertLogin', views.insertLogin, name='insertLogin'),
    path('loadRegister', views.loadRegister, name='loadRegister'),
    path('insertRegister', views.insertRegister, name='insertRegister'),
    path('updatePassword', views.updatePassword, name='updatePassword'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('insertForgotPassword', views.insertForgotPassword, name='insertForgotPassword'),

]
