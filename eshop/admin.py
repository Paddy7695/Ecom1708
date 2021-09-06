from django.contrib import admin
from .models import *


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','image']

class CategoryModeladmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerModeladmin(admin.ModelAdmin):
    list_display = ['name','email','phone','user']



admin.site.register(Product,ProductModelAdmin)
admin.site.register(Category,CategoryModeladmin)
admin.site.register(Customers,CustomerModeladmin)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(order_placed)
