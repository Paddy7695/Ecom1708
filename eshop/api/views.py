from rest_framework import viewsets
from eshop.api.serializers import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class CustomersApi(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class AddressApi(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

