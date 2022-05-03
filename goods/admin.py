from django.contrib import admin

from goods.models import StoreLocation,Product,Category,Merchant,ShippingAddress

# Register your models here.
admin.site.register(StoreLocation)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Merchant)
