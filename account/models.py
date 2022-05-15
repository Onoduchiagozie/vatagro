from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth import get_user_model




class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone=models.CharField(max_length=20)
    Active_Shipping_Address=models.ForeignKey('goods.ShippingAddress',on_delete=models.DO_NOTHING,
    blank=True,null=True
    
)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False)

    STATUS=(
        ('Buyer','Buyer'),
        ('Seller','Seller')
    )
    client_status=models.CharField(max_length=500,choices=STATUS)
    

    USERNAME_FIELD='email'


    def has_perm(self,perm,obj=None):
        return self.is_admin


    def __str__(self):
        return self.first_name
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff
    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


    objects=UserManager()

