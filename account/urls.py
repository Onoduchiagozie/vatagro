
from django.urls import path
from . import views

urlpatterns = [



                    path('createorder',views.create_order,name='createorder'),

    path('',views.home,name='home'),
                    path('logout',views.logout_request,name='logout'),
                   path('category/<pk>',views.category,name='category'),
        path('product_details/<pk>',views.product_details,name='product_details'),
        path('checkout',views.checkout,name='checkout'),
                path('addcart/<int:product_id>',views.add_cart,name='addcart'),
    path('removecart/<int:product_id>', views.remove_cart, name='removecart'),

    # path('login',views.login_request,name='login'),
        #         path('register',views.register,name='register'),

                     path('login/',views.MyLogin.as_view(),name='login'),  
                path('register',views.SignUpView.as_view(),name='register')


]
