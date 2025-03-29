from django.db import models

# Create your models here.
class foods(models.Model):
    Food_name= models.CharField(max_length=255)
    price= models.IntegerField()
    






    def __str__(self):
       return f"{self.Food_name} {self.price}"