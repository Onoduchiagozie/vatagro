from django.db import models


# noinspection PyCallingNonCallable
class StoreLocation(models.Model):
    
    name = models.CharField(max_length=20)

    states_list= (
                    ("Abia", " Abia"),                      
                    ( "Bauchi", "Bauchi",),
                    ( "Bayelsa","Bayelsa",),
                    ( "Benue", "Benue",),
                    ( "Borno",  "Borno",     ),
                  ("Cross River" ,"Cross River",),
                  ("Delta",   "Delta",   ),
                    ("Ebonyi",  "Ebonyi",  ),
                    ("Edo",    "Edo",    ),
                    ("Ekiti",  "Ekiti",  ),
                    ("Enugu",  "Enugu",   ),
                    ("FCT - Abuja","FCT - Abuja",),
                  ("Gombe",  "Gombe",  ),
                    ("Imo",    "Imo",    ),
                    ("Jigawa", "Jigawa", ),
                    ("Kaduna",  "Kaduna",  ),
                    ("Kano",    "Kano",       ),
                  ("Katsina","Katsina",),
                    ("Kebbi",   "Kebbi",      ),
                  ("Kogi",      "Kogi",    ),
                    ("Kwara",   "Kwara",   ),
                    ("Lagos",   "Lagos",   ),
                    ("Nasarawa","Nasarawa",),
                    ("Niger",   "Niger",      ),
                  ("Ogun",      "Ogun",    ),
                    ("ndo",     "ndo",     ),
                    ("Osun",    "Osun",    ),
                    ("Oyo",    "Oyo",    ),
                    ("Plateau","Plateau",),
                    ("Rivers",  "Rivers",  ),
                    ("Sokoto",  "Sokoto", ),
                    ("Taraba","Taraba",),
                    ("Yobe",    "Yobe",),
                  ("Zamfara","Zamfara")    ,
)         
    states=models.CharField(max_length=20,choices=states_list)
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.name

           

class Merchant(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
      return self.name
    



class ShippingAddress(models.Model):
    states_list= (
                    ("Abia", " Abia"),                      
                    ( "Bauchi", "Bauchi",),
                    ( "Bayelsa","Bayelsa",),
                    ( "Benue", "Benue",),
                    ( "Borno",  "Borno",     ),
                  ("Cross River" ,"Cross River",),
                  ("Delta",   "Delta",   ),
                    ("Ebonyi",  "Ebonyi",  ),
                    ("Edo",    "Edo",    ),
                    ("Ekiti",  "Ekiti",  ),
                    ("Enugu",  "Enugu",   ),
                    ("FCT - Abuja","FCT - Abuja",),
                  ("Gombe",  "Gombe",  ),
                    ("Imo",    "Imo",    ),
                    ("Jigawa", "Jigawa", ),
                    ("Kaduna",  "Kaduna",  ),
                    ("Kano",    "Kano",       ),
                  ("Katsina","Katsina",),
                    ("Kebbi",   "Kebbi",      ),
                  ("Kogi",      "Kogi",    ),
                    ("Kwara",   "Kwara",   ),
                    ("Lagos",   "Lagos",   ),
                    ("Nasarawa","Nasarawa",),
                    ("Niger",   "Niger",      ),
                  ("Ogun",      "Ogun",    ),
                    ("ndo",     "ndo",     ),
                    ("Osun",    "Osun",    ),
                    ("Oyo",    "Oyo",    ),
                    ("Plateau","Plateau",),
                    ("Rivers",  "Rivers",  ),
                    ("Sokoto",  "Sokoto", ),
                    ("Taraba","Taraba",),
                    ("Yobe",    "Yobe",),
                  ("Zamfara","Zamfara")    ,
)         
    state = models.CharField(max_length=50,choices=states_list)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
      return self.address

# AFTER CART PURCHASE
# class PurchasedProducts(models.Model):
#     purchased_product_name=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
#     state_Location_bought=models.foreighnkey
#     # tracking_no=
#     quantity=



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100)
    cat_image = models.ImageField(upload_to='photos/category',blank=True)
    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.TextField()
    product_catgeory = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    store_location = models.ForeignKey(
    StoreLocation, on_delete=models.DO_NOTHING,blank=True)

    per=(
      ('25 Litres','25 Litres'),
      ('50 Litres','50 Litres'),
      ('10 Litres','10 Litres'),
      ('25kg Bag','25kg Bag'),
      ('50kg Bag','50kg Bag'),
            ('Basket','Basket'),
    )
    measurment = models.CharField(max_length=20,choices=per)

    product_description = models.CharField(max_length=500,blank=True)
    quantity = models.IntegerField(blank=True)
    price = models.IntegerField()
    intra_state_shipping_fee = models.CharField(max_length=20,blank=True)
    inter_state_shipping_fee = models.CharField(max_length=20,blank=True)

    prod_image = models.ImageField(upload_to='photos/goods')
    stock = models.IntegerField(blank=True)
    farmername = models.ForeignKey(Merchant, on_delete= models.DO_NOTHING,blank=True)
    is_active = models.BooleanField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

