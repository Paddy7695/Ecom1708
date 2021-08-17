from django.db import models
from django.contrib.auth.models import User



class Customers (models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    phone = models.PositiveIntegerField()
    user = models.OneToOneField(User,on_delete= models.CASCADE)


    def __str__(self):
        return self.name


class Address (models.Model):
    city = models.CharField(max_length=70)
    area = models.CharField(max_length=70)
    pincode = models.PositiveIntegerField()
    customers = models.ForeignKey('Customers',on_delete=models.CASCADE,related_name='caddress',null=False)



    def __str__(self):
        return str(self.id)




class Cart (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Product (models.Model):
    name = models.CharField(max_length=70)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    discription = models.TextField()
    image = models.ImageField(upload_to='productimg',null=True)


    def __str__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(max_length=70)


    def __str__(self):
        return self.name



options=(
    ('accepted','accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
    ('delivered','delivered'),
    ('cancel','cancel'))

class order_placed (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customers = models.ForeignKey('customers',on_delete =models.CASCADE)
    product = models.ForeignKey('product',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    stutus = models.CharField(max_length=70,choices=options)



