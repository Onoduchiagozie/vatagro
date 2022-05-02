from django.contrib import admin

from goods.models import StoreLocation,Products,Category,Merchant

# Register your models here.
admin.site.register(StoreLocation)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Merchant)