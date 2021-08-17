from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


class SignUpform(UserCreationForm):
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



        '''
        def clean(self):
            category = Category.objects.get_or_create(
                category_text=self.cleaned_data.get('category'))
            self.cleaned_data['category'] = category
            return super(Productform, self).clean()labels = labels = {'name':'naame'}
        widgets = {'name' : forms.TextInput(attrs={'class':'form-control'})}
        ['name','price','category','discription','image']
'''