from django.db import models
from django.contrib.auth.models import User
import os
from twilio.rest import Client
import random





class Customers (models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    phone = models.PositiveIntegerField()
    user = models.OneToOneField(User,on_delete= models.CASCADE,null=True)



    def __str__(self):
        return self.name

    '''def save (self, *args, **kwargs) :

        number_list = [x for x in range(10)]
        numbers = []

        for i in range(5):
            num = random.choice(number_list)
            numbers.append(num)


        otpgen = "".join(str(item) for item in numbers)
        self.otp = otpgen
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = "AC82c88d935ff1fdf9d1789b68fc59dda5"
        auth_token = "5a5013942f906f910e08c8bc8daa0bf3"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="yetoy ka sms.{self.otp}",
            from_='+19402419784',
            to='+91{self.phone}'
        )

        print(message.sid)

        return super().save(*args,**kwargs)'''



class Address (models.Model):
    city = models.CharField(max_length=70)
    area = models.CharField(max_length=70)
    pincode = models.PositiveIntegerField()
    customers = models.ForeignKey('Customers',on_delete=models.CASCADE)



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
    stutus = models.CharField(max_length=70,choices=options,default='pending')



