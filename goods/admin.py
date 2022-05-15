from django.contrib import admin

from goods.models import  StoreLocation,Product,Category,ShippingAddress

# Register your models here.
admin.site.register(StoreLocation)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShippingAddress)
