


from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
            path('',views.account,name='account'),

        path('dashboard',views.dashboard,name='dashboard'),
        path('<pk>/profile',views.AuthorUpdateView.as_view(),name='profile'),
        path('shipping',views.shippingaddress,name='shippingaddress'),
        path('storelocation',views.storelocation,name='storelocation'),
        path('myproducts',views.myproducts,name='myproducts'),
                path('purchasedproducts',views.purchasedproducts,name='purchasedproducts'),




]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)