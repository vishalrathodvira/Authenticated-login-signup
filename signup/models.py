from django.db import models

# Create your models here.
class Saveuser(models.Model):
    studentname = models.CharField(max_length=50)
    mno = models.CharField(max_length=50)
    collegename = models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    cls= models.CharField(max_length=50)
    



