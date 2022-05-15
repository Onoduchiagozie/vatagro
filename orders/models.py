from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.




    
class OrderProducts(models.Model):
    user=models.ForeignKey('account.User',on_delete=models.DO_NOTHING)
    product_name=models.CharField(max_length=200)
    location=models.TextField()
    tracking_no=models.CharField(max_length=100)
    quantity=models.IntegerField()
    amount=models.IntegerField()
    Transaction_date=models.DateTimeField(auto_now_add=True)
    sold_by=models.CharField(max_length=100)
    package_mode=(
        ('Awaiting Packaging','Awaiting Packaging'),
        ('Packaged','Packaged'),
        ('On Delivery','On Delivery'),
        ('Delivered','Delivered'),
    )
    status=models.CharField(max_length=100,choices=package_mode,default='Awaiting Packaging')
    is_approved=models.BooleanField(default=False)


    def __str__(self):
        return self.tracking_no