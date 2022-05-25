import random
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import  logout
from django.contrib.auth.views import LoginView
from account.forms import ReviewForm, SignUpForm
from django.views.generic import  CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from account.models import User
from farmer.models import Cart, CartItem
from goods.models import Category, StoreLocation
from goods.models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from orders.models import OrderProducts, ReviewRating
import stripe
from django.conf import settings
from django.core.mail import send_mail

# CART FUNCTIONS


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('checkout')



def add_cart2(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('product_details',pk=product_id)



def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    else:
        cart_item.delete()

    return redirect('checkout')


def clear_cart(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.filter(cart=cart)
    cart_item.delete()
    return redirect('checkout')


def success(request, cart_items=None):
    # ADD PRODUCTS TO ORDERED PRODUCTS CART
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    for x in cart_items:
        today = OrderProducts(user=request.user,
                              product_name=x.product.product_name,
                              location=x.product.store_location.states,
                              tracking_no='Vatagro-' +
                              str(random.randint(100, 200)),
                              quantity=x.quantity,
                              amount=x.product.price*x.quantity,
                              sold_by=x.product.farmername
                              )
        today.save()
 


    
    cart_items.delete()
    return render(request, 'account/success.html')


def cancel(request):
    return render(request, 'account/cancel.html')


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=request.build_absolute_uri(
                    reverse('success')
                ) + "?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=request.build_absolute_uri(reverse('cancel')),
                payment_method_types=['card'],
                customer_email=request.user.email,
                mode='payment',
                line_items=[

                    {'price_data':  {'currency': 'ngn', 'product_data': {'name': x.product.product_name, },
                                     'unit_amount': x.product.price * 100},
                     'quantity': x.quantity,
                     } for x in cart_items

                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)





# CART & CHECKOUT PAGE
@login_required
def checkout(request, total=0, quantity=0, cart_items=None):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    userid = request.user
    current_user = get_object_or_404(User, pk=userid.id)
    shipping_total = 0
    shipping = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
        if current_user.Active_Shipping_Address.state == cart_item.product.store_location.states:
            shipping = cart_item.product.intra_state_shipping_fee
        else:
            shipping = cart_item.product.inter_state_shipping_fee
        shipping_total += int(shipping)

    tax = (2*total)/100
    grand_total = total+tax+int(shipping_total)
    user = request.user
    active_shipping = get_object_or_404(User, pk=user.id)
    context = {
        'quantity': quantity,
        'cart_items': cart_items,
        'address': active_shipping,
        'tax': tax,
        'grand_total': grand_total,
        'shipping': shipping,
        'shipping_total': shipping_total

    }

    return render(request, 'account/checkout.html', context)


# CATEGORY BROCHURE VIEWING(SORTA)
def category(request, pk):
    cat = Category.objects.all()
    main_page_category_header = Category.objects.get(pk=pk)
    product_category = Product.objects.filter(product_catgeory=pk)
    storelocat = StoreLocation.objects.all()

    # product_category=Product.objects.filter(store_location=pk)

    product_found_count = product_category.count()
    context = {
        "cat": cat,
        'main': main_page_category_header,
        'prod_cat': product_category,
        "store_state_list": storelocat,
        'prod_found': product_found_count,

    }
    return render(request, 'account/catgeory.html', context)


def category2(request, pk):
    cat = Category.objects.all()
    storelocations = StoreLocation.objects.all()
    main_page_state_header = StoreLocation.objects.get(pk=pk)
    product_category = Product.objects.filter(store_location=pk)
    product_found_count = product_category.count()
    context = {
        "cat": cat,
        'prod_cat': product_category,
        "store_state_list": storelocations,
        'prod_found': product_found_count,
        'state_name': main_page_state_header

    }
    return render(request, 'account/catgeory.html', context)


# SPECIFIC PRODUCT DETAIL
@login_required
def product_details(request, pk):
    selected_product = get_object_or_404(Product, pk=pk)
    in_cart = CartItem.objects.filter(
        cart__cart_id=_cart_id(request), product=selected_product)
    review = ReviewRating.objects.filter(
        product_id=selected_product.id, status=True)
    context = {
        "product": selected_product,
        "incart": in_cart,
        'review': review
    }
    return render(request, 'account/product_details.html', context)


@login_required
def search_product_details(request):
    id = request.POST.get('prod')
    selected_product = get_object_or_404(Product, pk=id)
    in_cart = CartItem.objects.filter(
        cart__cart_id=_cart_id(request), product=selected_product)
    review = ReviewRating.objects.filter(
        product_id=selected_product.id, status=True)
    context = {
        "product": selected_product,
        "incart": in_cart,
        'review': review
    }
    return render(request, 'account/product_details.html', context)


def review_rating(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(
                request, 'Thank You Your Review Has Been Updated.',)
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success = (
                    request, 'Thank You ,Your Review Has Been Submitted')
                return redirect(url)


# HOMEPAGE
def home(request):

    prod_category = Category.objects.all()
    sellers = User.objects.filter(staff=True)
    all_product = Product.objects.all()

    context = {
        'cat': prod_category,
        'seller': sellers,
        'product_list': all_product
    }
    return render(request, 'account/index.html', context)

# LOGOUT


def logout_request(request):
    logout(request)
    return redirect('home')

# LOGIN


class MyLogin(SuccessMessageMixin,LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('account')


# REGISTRATION


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
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
