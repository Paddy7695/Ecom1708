from django.urls import path,include
from eshop.api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('customersApi/', views.CustomersApi, basename='customers'),
router.register('addressapi/', views.AddressApi, basename='address')

urlpatterns = [

    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

]