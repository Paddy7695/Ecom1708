from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


class SignUpform(UserCreationForm):
    usertype_choices =[('Seller','Seller'),
                ('Buyer','Buyer')
              ]

    usertype = forms.ChoiceField(choices=usertype_choices)

    class Meta:
        model = User
        fields = ['username','first_name','last_name']





class Customersform(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'





class UserLoginform(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','discription','image']


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Customerform(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name','email','phone']

class Addressform(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'



class OrderPlacedform(forms.ModelForm):
    class Meta:
        model = order_placed
        fields = ['id','stutus']



        '''
        def clean(self):
            category = Category.objects.get_or_create(
                category_text=self.cleaned_data.get('category'))
            self.cleaned_data['category'] = category
            return super(Productform, self).clean()labels = labels = {'name':'naame'}
        widgets = {'name' : forms.TextInput(attrs={'class':'form-control'})}
        ['name','price','category','discription','image']
'''