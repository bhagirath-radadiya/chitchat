from django.db import models


# Create your models here.

class Loginmaster(models.Model):
    loginUserName = models.CharField(max_length=100, null=False)
    loginPassword = models.CharField(max_length=50, null=False)
    loginRole = models.CharField(max_length=50, null=False)


class Usermaster(models.Model):
    userName = models.CharField(max_length=100, null=False)
    userMobileNo = models.CharField(max_length=10, null=True, blank=True)
    userBirthdate = models.DateField(null=True, blank=True)
    userAddress = models.CharField(max_length=1000, null=True, blank=True)
    userFacebook = models.CharField(max_length=1000, null=True, blank=True)
    userTwitter = models.CharField(max_length=1000, null=True, blank=True)
    userInstagram = models.CharField(max_length=1000, null=True, blank=True)
    userLinkedin = models.CharField(max_length=1000, null=True, blank=True)
    userProfilePhoto = models.FileField(default='apple-touch-icon.png')
    user_LoginId = models.ForeignKey(Loginmaster, on_delete=models.CASCADE, db_column='user_LoginId')
