from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user   =  models.OneToOneField(User, on_delete=models.CASCADE)
    fine   = models.IntegerField(null=True,default=True) 
    photo  = models.ImageField(upload_to="users",null=True,blank=True) 
      

class Record(models.Model):
    acc     = models.CharField(max_length=50)
    issue   = models.TimeField(null=True,blank=True)
    back    = models.TimeField(null=True,blank=True)
    user    = models.ForeignKey(User,on_delete= models.CASCADE)
    def __str__(self):
        return self.acc+"("+self.user.username+")"