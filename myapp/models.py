from django.db import models

# Create your models here.
class log(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=50)

class contacts(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    message = models.CharField(max_length=500)
    additionaldetails = models.CharField(max_length=50)