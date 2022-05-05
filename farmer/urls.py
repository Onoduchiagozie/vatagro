


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




        path('storelocation',views.storelocation,name='storelocation'),


        path('myproducts',views.myproducts,name='myproducts'),


        path('purchasedproducts',views.purchasedproducts,name='purchasedproducts'),


        path('new',views.new,name='new'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)