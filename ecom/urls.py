"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from eshop import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('api/',include('eshop.api.urls')),
    path('admin/', admin.site.urls),
    path('store/', views.store,name='store'),
    path('', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('cart/', views.showcart, name='showcart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove/', views.remove, name='remove'),
    path('pluscart/', views.pluscart, name='pluscart'),
    path('minuscart/', views.minuscart, name='minuscart'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('orders/', views.orders, name='orders'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('customerinfo/', views.customerinfo, name='customerinfo'),
    path('add_address/', views.add_address, name='add_address'),
    path('payment/',views.payment,name='payment'),
    path('change_status/',views.change_status,name='change_status')
    # path('search/',views.search,name='search')




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
