from django.db import models


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







class ReviewRating(models.Model):
    product=models.ForeignKey('goods.Product',on_delete=models.CASCADE)
    user=models.ForeignKey('account.User',on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,blank=True)
    review=models.TextField(max_length=500,blank=True)
    rating=models.FloatField()
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)