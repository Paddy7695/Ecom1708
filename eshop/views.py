from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required




def home (request):
    return render(request, 'home.html')




def store (request):

    categories = Category.objects.all()
    categoryID=request.GET.get('category')
    print(categoryID)
    if categoryID:
        products = Product.objects.filter(category = categoryID)
    else:
        products = Product.objects.all()

    context = {'products': products,'categories':categories}
    return render(request, 'store.html',context)

@login_required(login_url='/login/')
def add_product (request):
    if request.user.is_superuser:
        user = request.user
        print("---------hi--------")
        if request.method == 'POST':


            categoryID = request.POST.get("category")
            print(categoryID)
            category = Category.objects.get(id=categoryID)

            form = Productform(request.POST,request.FILES)

            if form.is_valid():
                product = form.save(commit=True)
                product.category_id = categoryID
                product.save()




            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/')

        categorys = Category.objects.all()
        form = Productform()
        context = {'form':form,'categorys':categorys}
        return render(request, 'add_product.html',context)

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




def signup(request):
    form = SignUpform()
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
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
                messages.success(request, 'logged in successful')
                return HttpResponseRedirect('/store/')

    form = UserLoginform()
    context = {'form':form}
    return render(request, 'login.html',context)



@login_required(login_url='/login/')
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
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
            print(c)
            quantity = c.quantity
            price = c.product.price*quantity
            print(quantity)
            print((price))
            sum = sum+price
            print(sum)

        context = {'cart':cart,'total':sum}
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
   '''cartid = request.GET.get('cartid')
    print(cartid)
    cartobj = Cart.objects.get(id=cartid)
    quantity = cartobj.quantity
    quantity =cqty+1'''
   quantity = request.GET.get('quantity')
   print(quantity)
   quantity=quantity+1
   cart = cart (user = user, product = product,quantity= quantity)
   cartobj.save()

@login_required(login_url='/login/')
def remove(request):

    if request.user.is_authenticated:
        cartid = request.GET.get('cartid')
        print(cartid)
        cartobj = Cart.objects.get(id=cartid)
        print(cartobj)

        cartobj.delete()
        return HttpResponseRedirect ('/cart/')



def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        customers = Customers.objects.filter(id = user.id)
        print(customers)
        address = Address.objects.filter(customers__id = user.id)



        context = {'customers':customers,'address': address}
        return render(request, 'profile.html',context)

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
        address = Address.objects.all()
        context = {'cart': cart,'sum': sum,'total': total,'address': address}
        return render(request, 'checkout.html',context)

@login_required(login_url='/login/')
def payment_done(request):
    if request.user.is_authenticated:
        user = request.user
        customers = Customers.objects.get(user=user)
        print(customers)
        cart = Cart.objects.filter(user=user)
        for c in cart:
            order_place = order_placed(user = user ,customers = customers,product=c.product,quantity=c.quantity)
            order_place.save()
            c.delete()

        return HttpResponseRedirect('/orders')


@login_required(login_url='/login/')
def orders (request):
    if request.user.is_authenticated:
        user = request.user
        order_place = order_placed.objects.filter(user = user)
        context = {'orders_placed':order_place}
        return render(request,'orders.html',context)








