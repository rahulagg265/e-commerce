from email.headerregistry import Address
from email.mime import image

# from typing_extensions import Self
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#store-product models

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField()
    desc = models.TextField()
    image = models.ImageField(null=False)
    class Meta:
        db_table = 'product'
        

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url         

# customer - models

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.name


# order model
class Order(models.Model):
    # id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, null=True)

    @property
    def carttotal(self):
        orderitem = self.orderitems_set.all()
        total = sum([items.gettotal for items in orderitem])
        return total

    @property
    def cartitemtotal(self):
        orderitem = self.orderitems_set.all()
        total = sum([items.quantity for items in orderitem])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitems_set.all()
        return shipping

     

    

  

 

# orderitems model
class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     db_table = 'orderItems'

    def __int__(self):
        return self.id    

    @property
    def gettotal(self):
        total = self.product.price * self.quantity 
        return total         



Statechoices = (
    ("1", "Delhi"),
    ("2", "mumbai"),
    ("3", "goa"),
    ("4", "bihar"),
    ("5", "Punjab"),
    ("7", "Rajasthan"),
    
)
class Shippingaddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True,blank=True)
    Address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50,choices=Statechoices,default=1)

    
    def __int__(self):
        return self.order

