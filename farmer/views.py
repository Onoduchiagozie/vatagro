
from django.shortcuts import get_object_or_404, redirect, render
from farmer.models import Cart, CartItem

from goods.models import Product, ShippingAddress
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView
from account.models import User











# Create your views here.
def account(request):
    files=get_object_or_404(pk=1)
    context={
        
    }
    return render(request,'farmer/account.html',context)



def dashboard(request):
    return render(request,'farmer/dashboard.html')


class UserUpdateView(UpdateView):
    model=User
    fields = ['first_name','last_name','email','phone','client_status','Active_Shipping_Address']
    success_url = '/'
    template_name = 'farmer/profile.html'




# SHIPPING_ADDRESS
class ShippingAddressUpdateView(UpdateView):
    model=ShippingAddress
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/shippingaddress.html'

class ShippingAddressCreateView(CreateView):
    model=ShippingAddress
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/createnew.html'

class ShippingAddressListView(ListView):
    model=ShippingAddress
    # fields = '__all__'
    success_url = '/'
    template_name = 'farmer/listshippingaddress.html'
    context_object_name='object'


# MY_PRODUCTS
class MyProductsListView(ListView):
    model=Product
    # fields = '__all__'
    success_url = '/'
    template_name = 'farmer/myproducts.html'
    context_object_name='object'

class MyProductsCreateView(CreateView):
    model=Product
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/newmyproducts.html'


class ProductsUpdateView(UpdateView):
    model=Product
    fields = '__all__'
    success_url = '/'
    template_name = 'farmer/updateproducts.html'


# FARMERONLY
def storelocation(request):
    return render(request,'farmer/storelocation.html')



# LISTVIEW TABLE
def purchasedproducts(request):
    return render(request,'farmer/purchasedproduct.html')

def new(request):
    return  render(request,'farmer/createnew.html')