from django.contrib import admin

# Register your models here.
from .models import OrderProducts

admin.site.register(OrderProducts)