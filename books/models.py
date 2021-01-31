from django.db import models

# Create your models here.

class Book(models.Model):

    title       =  models.CharField(max_length= 50)
    author      =  models.CharField(max_length= 50)
    accessNo    =  models.CharField(max_length= 50,primary_key=True)
    availible   =  models.BooleanField(default=True)
    image       =  models.ImageField(upload_to="images")
    def __str__(self):
        return self.title