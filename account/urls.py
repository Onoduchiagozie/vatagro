
from django.urls import path
from . import views

urlpatterns = [
                    path('success/',views.success,name='success'),
                    path('cancel/',views.cancel,name='cancel'),

path('cart_reload/',views.cart_reload,name='cart_reload' ),

                    path('config/',views.stripe_config,name='config'),
                    path('create-checkout-session/', views.create_checkout_session), # new
                    path('clearcart',views.clear_cart,name='clearcart'),
                    path('',views.home,name='home'),
                    path('logout',views.logout_request,name='logout'),
                    path('category/<pk>',views.category,name='category'),
                    path('category/<pk>',views.category2,name='category2'),
                    path('product_details/<pk>',views.product_details,name='product_details'),
                    path('product_details2',views.product_details2,name='product_details2'),
                    path('checkout',views.checkout,name='checkout'),
                    path('addcart/<int:product_id>',views.add_cart,name='addcart'),
                    path('removecart/<int:product_id>', views.remove_cart, name='removecart'),
                    path('submit_review/<int:product_id>', views.review_rating,name='submit_review'),
                    path('login/',views.MyLogin.as_view(),name='login'),  
                    path('register',views.SignUpView.as_view(),name='register'),

                    #path('login',views.login_request,name='login'),
                    # path('register',views.register,name='register'),




]
