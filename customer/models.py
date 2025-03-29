from django.db import models

class Loginmodel(models.Model):
    username = models.EmailField(unique= True, blank=True)
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    