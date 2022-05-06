from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.views  import LoginView
from account.forms import SignUpForm
from django.views.generic import TemplateView,ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
from account.models import User
from farmer.models import Cart, CartItem
from goods.models import Category, StoreLocation
from goods.models import Product
from django.db.models import F
from django.contrib.auth import get_user,get_user_model

# NO MATTER WHAT YOU DO LOGIN OR NOT /ADD 1 MILL OR NOT / ITS STILL THE SAME CART 
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
    
def add_cart(request,product_id):
    product= Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity +=1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()
   
    return redirect('checkout')











def checkout(request,total=0,quantity=0,cart_items=None):

    cart=Cart.objects.get(cart_id=_cart_id(request))
    cart_items=CartItem.objects.filter(cart=cart)
    userid=request.user
    current_user=get_object_or_404(User,pk=userid.id)
    shipping_total=0
    for cart_item in cart_items:
        total+=(cart_item.product.price * cart_item.quantity)
        quantity+= cart_item.quantity
        if current_user.Active_Shipping_Address.state == cart_item.product.store_location.states:
            shipping=cart_item.product.intra_state_shipping_fee
        else:
            shipping=cart_item.product.inter_state_shipping_fee
        shipping_total+=int(shipping)

    
    tax=(2*total)/100
    grand_total=total+tax+int(shipping_total)
    user=request.user
    active_shipping=get_object_or_404(User,pk=user.id)
    context={
        'quantity':quantity,
        'cart_items':cart_items,
        'address':active_shipping,
        'tax':tax,
        'grand_total':grand_total,
        'shipping':shipping,
        'shipping_total':shipping_total

    }
 
    return render(request,'account/checkout.html',context)


def category(request,pk):
    cat=Category.objects.all()
    main_page_cat=Category.objects.filter(pk=pk)
    product_category=Product.objects.filter(product_catgeory=pk)
    storelocat=StoreLocation.objects.all()
    context={
        "cat":cat,
        'main':main_page_cat,
        'prod_cat':product_category,
        "store_state_list":storelocat
    }
    return render(request,'account/catgeory.html',context)


def product_details(request,pk):
    selected_product= get_object_or_404(Product,pk=pk) 
    context={
        "product":selected_product,
            }
    return render(request,'account/product_details.html',context)

def home(request):
    prod_cat=Category.objects.all()
    sellers=User.objects.filter(staff=True)
    context={
        'cat':prod_cat,
        'seller':sellers
    }
    return render(request,'account/index.html',context)

def logout_request(request):
    logout(request)
    return redirect('home')

class MyLogin(LoginView):
    template_name='account/login.html'
    success_url = reverse_lazy('home')


# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				return redirect("home")
		
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request, "account/login.html",{"form":form})


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'account/register.html'

# def register(request):
#     if request.method == 'POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email=form.cleaned_data.get('email')
#             password=form.cleaned_data.get('password')
#             user=authenticate(email=email,password=password)
#             login(request,user)
#             return redirect('login')
#     else:
#         form=SignUpForm()
#     return render(request,'account/register.html',{'form':form})
