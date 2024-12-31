from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin ,BaseUserManager,UserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CostumUserManager(UserManager):
     
    def create_user(self, email, mobile, password=None,**extra_fields):
        """
        Creates and saves a User with the given email, mobile and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            mobile=mobile,
        )
        user.is_superuser = True
        user.is_staff= True
        user.is_active=True
        user.save(using=self._db)
        return user

class User(AbstractUser,PermissionsMixin):

    Role_CHOICES=[
        ('customer','Customer'),
        ('vendor','Vendor'),
        ('driver','Driver')
    ]
   
    username=None
    mobile = models.BigIntegerField(_('phone number'),unique=True,null=True,blank=False,
                                  validators=[
                                      validators.RegexValidator(r'^989[0-3,9]\d{8}$',message='enter a valid mobile number'
                                                                
                                                                )
                                  ],
                                  error_messages={
                                      'unique':_("A user with this mobile number already exists .")
                                  }
                                  
                                  )
    email = models.EmailField(_("email address"), blank=False,null=False,unique=True)

    role=models.CharField(max_length=10,choices=Role_CHOICES,null=True)
    
    REQUIRED_FIELDS=["mobile"]
    USERNAME_FIELD="email"

    objects=CostumUserManager()




class Costumer(models.Model):
        
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='costumer')
    location=models.TextField(max_length=300,null=True,blank=False)


#move to Vendor app

# class Vendor(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     store_address=models.TextField(max_length=300,null=True,blank=False)
#     store_phone=models.CharField(max_length=15)
#     # store_logo=models.ImageField()
#     store_name=models.CharField(max_length=40,null=True,blank=False)
#     business_license=models.FileField()
#     is_verified=models.BooleanField(default=False)
#     longitude=models.FloatField(null=True , blank=True)
#     latitude=models.FloatField(null=True , blank=True)
    


class Driver(models.Model):

    VEHICLE_CHOICES=[
        ('car','Car'),
        ('motorbike','Motorbike')
    ]


    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=30,null=True)
    license_plate=models.CharField(max_length=10,unique=True)
    vehicle_type=models.CharField(max_length=50 , choices=VEHICLE_CHOICES)
    # driver_license=models.FileField()
    phone_number=models.CharField(max_length=15)






                                
                
