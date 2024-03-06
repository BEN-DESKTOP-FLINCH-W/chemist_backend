from django.db import models
from django.utils import timezone

#products
class Products(models.Model):
    name= models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    instock= models.IntegerField()
    price= models.IntegerField()

    def __str__(self):
        return self.name +' '+ self.category +' '+ str(self.instock) +' '+ str(self.price)
    

#categories  
class Categories(models.Model):
    name= models.CharField(max_length=70)

    def __str__(self):
        return self.name


#sales
class Sales(models.Model):
    name= models.CharField(max_length=70)
    category= models.CharField(max_length=70, null=True)
    unit_price= models.IntegerField()
    quantity= models.IntegerField(null=True)
    total= models.IntegerField()
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name +' '+ str(self.unit_price) +' '+ str(self.total) +' '+ str(self.quantity) +' '+ str(self.date)

#expenses
class Expenses(models.Model):
    name= models.CharField(max_length=70)
    amount= models.IntegerField()
    date=date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name +' '+ str(self.amount) +' '+ str(self.date)
#users  
class Users(models.Model):
    name= models.CharField(max_length=70)
    email= models.CharField(max_length=70)
    password =models.CharField(max_length=70)

    def __str__(self):
        return self.name +' '+ self.email +' '+ self.password
