from django.db import models
from login.models import Loginmaster, Usermaster


# Create your models here.

class Msgmaster(models.Model):
    msg_From = models.ForeignKey(Loginmaster, on_delete=models.CASCADE, related_name='msg_From', db_column='msg_From')
    msg_To = models.ForeignKey(Loginmaster, on_delete=models.CASCADE, related_name='msg_To', db_column='msg_To')
    msg = models.CharField(max_length=1000, blank=True)
    msgSendTime = models.TimeField(null=True)
    msgSendDate = models.DateField(null=True)
    msgSendBy = models.IntegerField(null=True)
