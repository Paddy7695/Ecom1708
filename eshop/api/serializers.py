from rest_framework import serializers
from eshop.models import *



class CustomersSerializer (serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class AddressSerializer (serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CartSerializer (serializers.ModelSerializer):
    class meta:
        Model = Cart
        fields = '__all__'

