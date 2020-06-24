from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class RegularPizza (models.Model):
    name= models.CharField(max_length=64)
    small= models.DecimalField(max_digits=4, decimal_places=2 )
    large= models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class SicilianPizza (models.Model):
    name= models.CharField(max_length=64)
    small= models.DecimalField(max_digits=4,decimal_places=2)
    large= models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return f"{self.name}-{self.small}-{self.large}"

class Topping(models.Model):
    name= models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Sub (models.Model):
    name= models.CharField(max_length=64)
    small= models.DecimalField(max_digits=4,decimal_places=2)
    large= models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return f"{self.name}-{self.small}-{self.large}"

class Pasta (models.Model):
    name= models.CharField(max_length=64)
    price= models.DecimalField(max_digits=4,decimal_places=2)
 
    def __str__(self):
        return f"{self.name}-{self.price}"

class Salads (models.Model):
    name= models.CharField(max_length=64)
    price= models.DecimalField(max_digits=4,decimal_places=2)
 
    def __str__(self):
        return f"{self.name}-{self.price}"

class DinnerPlatter (models.Model):
    name= models.CharField(max_length=64)
    small= models.DecimalField(max_digits=4,decimal_places=2)
    large= models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return f"{self.name}-{self.small}-{self.large}"

class Orders(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    OrderNo= models.DecimalField(max_digits=4,decimal_places=2)
    OrderdateTime= models.DateTimeField()
    Item= models.CharField(max_length=255)
    OrderTotal= models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.username}-{self.OrderNo}-{self.OrderdateTime}-{self.Item}-{self.OrderTotal}"

class Items(models.Model):
    #OrderNo= models.ForeignKey(Orders,on_delete=models.CASCADE)
    OrderNo= models.IntegerField()
    Price= models.DecimalField(max_digits=4,decimal_places=2)
    Item = models.CharField(max_length=255)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Topping= models.CharField(max_length=255, default='NA')

    def __str__(self):
        return f"{self.OrderNo}-{self.Price}-{self.Item}-{self.username}-{self.Topping}"

class User_order(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    order_number=models.IntegerField()
    topping_allowance=models.IntegerField(default=0)
    status=models.CharField(max_length=64,default='initiated')
    def __str__(self):
        return f"{self.username} - {self.order_number} - {self.status} Topping_allowance: {self.topping_allowance}"

class Order_counter(models.Model):
    counter=models.IntegerField()

    def __str__(self):
        return f"Order no: {self.counter}  "