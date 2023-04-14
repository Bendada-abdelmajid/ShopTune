from django.db import models
from django.contrib.auth.models import User
from shopkeeper.models import pruduct

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, blank=True,  on_delete= models.CASCADE )
    full_name=models.CharField(max_length=150,blank=True)
    Customer_phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=150,blank=True, null=True)

    saved= models.ManyToManyField(
        pruduct, related_name="saveds",blank=True)
    def __str__(self):
        return self.user.username
   
    
        
   