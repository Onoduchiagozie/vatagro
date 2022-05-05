from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.views  import LoginView
from account.forms import SignUpForm
from django.views.generic import TemplateView,ListView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
from account.models import User
from goods.models import Category, StoreLocation
from goods.models import Product
from django.db.models import F



def checkout(request):
    return render(request,'account/checkout.html')


def category(request,pk):
    cat=Category.objects.all()
    main_cat=Category.objects.filter(pk=pk)
    product_category=Product.objects.filter(product_catgeory=pk)
    store=get_object_or_404(StoreLocation,pk=pk)
    storelocat=StoreLocation.objects.all()
    context={
        "cat":cat,
        'main':main_cat,
        'prod_cat':product_category,
        "state":store,
        "store_state_list":storelocat
    }
    return render(request,'account/catgeory.html',context)


def product_details(request,pk):
    selected_product= get_object_or_404(Product,pk=pk) 
    store=get_object_or_404(StoreLocation,pk=pk)
    context={
        "product":selected_product,
        "store":store
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
