from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from datetime import timedelta,date



def home (request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html',context)




def store (request):

    categories = Category.objects.all()
    categoryID=request.GET.get('category')
    qry = request.GET.get('search')
    print(categoryID)
    if categoryID:
        products = Product.objects.filter(category = categoryID)
    elif qry :
        # products = Product.objects.filter(name__contains=qry)
        products = [item for item in Product.objects.all() if qry in item.name.lower()  or qry in item.discription.lower()]
        # or qry in item.price or qry in item.category

    else:
        products = Product.objects.all()

    context = {'products': products,'categories':categories}
    return render(request, 'store.html',context)



@login_required(login_url='/login/')
def add_product (request):
    user = request.user
    print("---------hi--------")
    if request.method == 'POST':
        categoryID = request.POST.get("category")

        form = Productform(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=True)
            product.category_id = categoryID
            product.save()
        messages.success(request, 'Form submission successful')
        return HttpResponseRedirect('/home/')

    categorys = Category.objects.all()
    form = Productform()
    context = {'form':form,'categorys':categorys}
    return render(request, 'add_product.html',context)


@login_required(login_url='/login/')
def customerinfo(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            # form = Customerform(request.POST)
            # print(form)
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            print(phone)

            customer = Customers (name = name,email=email,phone=phone,user=user)
            customer.save()

            # if form.is_valid():
            #     print("-------------------------------------------------")
            #     customer = form.save(commit=True)
            #     customer.User = user
            #     customer.save()
            return HttpResponseRedirect('/profile/')

        form = Customerform()
        context = {'form':form}
        return render(request, 'customerinfo.html',context)





@login_required(login_url='/login/')
def add_category (request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Categoryform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/home/')

        form = Categoryform()
        context = {'form':form}
        return render(request, 'add_category.html',context)



import os
from twilio.rest import Client
def signup(request):
    form = SignUpform()

    if request.method == 'POST':
        form = SignUpform(request.POST)
        usertype = request.POST.get('usertype')
        print("------------------------------------------")
        print(usertype)
        if form.is_valid():
            User = form.save(commit=True)

            if usertype == 'Buyer':
                group = Group.objects.get(name ='Buyer')
                User.groups.add(group)

            elif usertype == 'Seller':
                group = Group.objects.get(name ='Seller')
                User.groups.add(group)

            account_sid = "AC82c88d935ff1fdf9d1789b68fc59dda5"
            auth_token = "5a5013942f906f910e08c8bc8daa0bf3"
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body="Ecom Account created sucessfulley ",
                from_='+19402419784',
                to='+917620233186'
            )

            print(message.sid)

            messages.success(request, 'Form submission successful')

            return HttpResponseRedirect('/login/')

    context = {'form':form}
    return render(request, 'signup.html',context)



def userlogin(request):

    if request.method == 'POST':
        form = UserLoginform(request,request.POST)
        print('-----------------------------------------')
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            if user is not None:
                login(request, user)
                messages.success(request, 'logged out successful')
                return HttpResponseRedirect('/store/')

    form = UserLoginform()
    context = {'form':form}
    return render(request, 'login.html',context)



@login_required(login_url='/login/')
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        td =timedelta(days=10)
        d = date.today()
        shiping = d+td

        cartID = request.GET.get('cartid')

        '''productid = request.GET.get('productid')
        product = Product.objects.get(id=productid)


        if cartID:
            quantityadd = int(request.GET.get('quantityadd'))
            a=1
            print(quantityadd+a)
            quantity=quantityadd+1
            cart=Cart(id=cartID,product=product,quantity=quantity)
            cart.save()
        else:
            quantitymin = int(request.GET.get('quantitymin'))
            a=1
            print(quantitymin-a)
            quantity=quantityadd-1
            cart=Cart(id=cartID,product=product,quantity=quantity)
            cart.save()
'''
        sum=0
        for c in cart:
            #print(c)
            quantity = c.quantity
            price = c.product.price*quantity
            #print(quantity)
            #print((price))
            sum = sum+price
            #print(sum)

        context = {'cart':cart,'total':sum,'shipping':shiping}
        return render(request, 'cart.html',context)


@login_required(login_url='/login/')
def add_to_cart(request):
    if request.user.is_authenticated:
        print("-------------------------------------------")
        productID = request.GET.get('productid')
        #print(productID)
        product = Product.objects.get(id = productID)
        #print(product)

        user = request.user

        cart = Cart(user = user, product = product)
        cart.save()
        return HttpResponseRedirect ('/cart/')



@login_required(login_url='/login/')
def pluscart (request):

   '''user = request.user
   prodId = request.GET.get('productid')
   print(prodId)
   product = Product.objects.get(id=prodId)
   cart = Cart (user = user, product = product,quantity= quantity)
   cart.save()
   '''
   prodquantity = request.GET.get('productqty')
   print(prodquantity)

   cartid = request.GET.get('cartid')
   print(cartid)
   cart = Cart.objects.get(id = cartid)
   print(cart)
   quantityadd = int(prodquantity)+1
   print(quantityadd)

   cart.quantity = quantityadd

   cart.save()

   return HttpResponseRedirect('/cart/')



def minuscart (request):

    prodquantity = request.GET.get('productqty')
    print(prodquantity)

    cartid = request.GET.get('cartid')
    print(cartid)
    cart = Cart.objects.get(id = cartid)
    print(cart)
    quantityadd = int(prodquantity)-1
    print(quantityadd)

    cart.quantity = quantityadd

    cart.save()

    return HttpResponseRedirect('/cart/')


@login_required(login_url='/login/')
def remove(request):

    if request.user.is_authenticated:
        cartid = request.GET.get('cartid')
        print(cartid)
        cartobj = Cart.objects.get(id=cartid)
        print(cartobj)

        cartobj.delete()
        return HttpResponseRedirect ('/cart/')



@login_required(login_url='/login/')
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def payment(request):
    total=100
    return render(request,'payment.html',{'total':total})



@login_required(login_url='/login/')
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.id)
        # customers = Customers.objects.get(name = 'rani chavan')
        customers = Customers.objects.get(user_id = user.id)
        # customers = Customers.objects.get(name = 'raja chavan')
        print(customers)

        # address = Address.objects.get(id = 1)
        # address = Address.objects.get(customers__user_id=customers.user.id)

        # address = Address.objects.filter(customers__id = customers.id)

        # address = Address.objects.filter(customers__id = user.id)
        address = Address.objects.filter(customers__user_id = user.id)
        # address = Address.objects.filter(customers_id = 'customers_user' )


        context = {'customers':customers,'address': address}
        return render(request, 'profile.html',context)


@login_required(login_url='/login/')
def add_address(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Addressform(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/profile/')
        form = Addressform()
        context = {'form':form}
        return render(request, 'add_address.html',context)





@login_required(login_url='/login/')
def checkout(request):
    if request.user.is_authenticated:
        custid = request.GET.get('custid')
        print(custid,"----------------------------------------------------------")
        user = request.user
        cart = Cart.objects.filter(user=user)
        sum=0
        for c in cart:
            print(c)
            quantity = c.quantity
            price = c.product.price * quantity
            print(quantity)
            print((price))
            sum = sum+price
            print(sum)
        total = sum+70
        address = Address.objects.filter(customers_id=custid)
        context = {'cart': cart,'sum': sum,'total': total,'address': address}
        return render(request, 'checkout.html',context)



@login_required(login_url='/login/')
def payment_done(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        print(type(user.id))
        try:
            customers = Customers.objects.get(user = user.id)
            print(customers)
        except:
            return HttpResponse("add customer info and address info")

        cart = Cart.objects.filter(user=user)
        for c in cart:
            order_place = order_placed(user = user ,customers = customers, product=c.product, quantity = c.quantity)
            order_place.save()
            c.delete()
        return HttpResponseRedirect('/payment')


@login_required(login_url='/login/')
def orders (request):
    if request.user.is_authenticated:
        user = request.user
        order_place = order_placed.objects.filter(user = user)
        context = {'orders_placed':order_place}
        return render(request,'orders.html',context)


@login_required(login_url='/login/')
def change_status (request):
    if request.user.is_authenticated:
        form = OrderPlacedform()
        context = {'form':form}
        return render(request,'change_status.html',context)














