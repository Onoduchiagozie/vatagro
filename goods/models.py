from django.db import models


class StoreLocation(models.Model):
    pass
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.CharField(max_length=100)
    cat_image=models.ImageField(upload_to='./')

    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_name=models.TextField()
    product_catgeory=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    product_store=models.ForeignKey(StoreLocation,on_delete=models.DO_NOTHING)
    measurment=models.TextChoices()
    quantity=models.IntegerChoices()
    price=models.IntegerField()
    shipping_cost=models.IntegerChoices()
    prod_image=models.ImageField()
    stock =models.IntegerField()

    def __str__(self):
        return self.product_name
    pass

