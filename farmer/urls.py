


from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
        path('',views.account,name='account'),
        path('dashboard',views.dashboard,name='dashboard'),


        path('<pk>/profile',views.UserUpdateView.as_view(),name='profile'),


        path('<pk>/UpdateShipping',views.ShippingAddressUpdateView.as_view(),name='shippingaddress'),
        path('createnewshipping',views.ShippingAddressCreateView.as_view(),name='newshippingaddress'),
        path('shippinglist',views.ShippingAddressListView.as_view(),name='shippinglist'),


        path('myproducts',views.MyProductsListView.as_view(),name='myproducts'),
        path('newproducts',views.MyProductsCreateView.as_view(),name='newproducts'),
        path('<pk>/updateproducts',views.ProductsUpdateView.as_view(),name='updateproducts'),





        path('storelocation',views.storelocation,name='storelocation'),




        path('purchasedproducts',views.purchasedproducts,name='purchasedproducts'),


        path('new',views.new,name='new'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)