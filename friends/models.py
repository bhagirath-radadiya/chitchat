from django.db import models
from login.models import Loginmaster, Usermaster


# Create your models here.

class FriendRequestmaster(models.Model):
    friendRequest_To = models.ForeignKey(Loginmaster, on_delete=models.CASCADE, related_name='friendRequest_To',
                                         db_column='friendRequest_To')
    friendRequest_From = models.ForeignKey(Loginmaster, on_delete=models.CASCADE, related_name='friendRequest_From',
                                           db_column='friendRequest_From')
    friendRequest_MSG = models.CharField(max_length=1000, null=False, blank=True)
    friendRequest_Action = models.CharField(max_length=50, null=False)
