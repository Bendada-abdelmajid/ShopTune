import imp
from django.db import models
from shopkeeper.models import pruduct
from django.contrib.auth.models import User


# Create your models here.
class OrdedrItem(models.Model):
    product = models.ForeignKey(
        pruduct, related_name="order_products", on_delete=models.CASCADE)
    price =models.DecimalField(max_digits=5, decimal_places=2,)
    qty=models.IntegerField()
    color=models.CharField(max_length=200,blank=True, null=True)
    size=models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return str(self.qty) + " " + self.product.title
class OrdedrOption(models.Model):
    name=models.CharField(max_length=200,blank=True, null=True)
    discription=models.CharField(max_length=200,blank=True, null=True)
    price =models.DecimalField(max_digits=5, decimal_places=2,)
    def __str__(self):
        return str(self.name)
class Ordedr(models.Model):
    customer=models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE) 
    address=models.CharField(max_length=200)    
    contry=models.CharField(max_length=200)      
    city=models.CharField(max_length=200)     
    postal=models.CharField(max_length=200)       
    ordedrOption = models.ForeignKey(
        OrdedrOption, related_name="OrdedrOption", on_delete=models.CASCADE)
    total_price =models.DecimalField(max_digits=7, decimal_places=2,)
    products = models.ManyToManyField(
        OrdedrItem, related_name="order_products",blank=True)
    oreder_date=models.DateTimeField(auto_now_add=True, )
    has_seen = models.BooleanField(default=False)
    complet = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username

    def add_order(self, prod):
        if not prod in self.products.all():
            self.products.add(prod)
            

    