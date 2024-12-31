from django.db import models
from users.models import User
# Create your models here.



class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    store_address=models.TextField(max_length=300,null=True,blank=False)
    store_phone=models.CharField(max_length=15)
    # store_logo=models.ImageField()
    store_name=models.CharField(max_length=40,null=True,blank=False)
    business_license=models.FileField()
    is_verified=models.BooleanField(default=False)
    longitude=models.FloatField(null=True , blank=True)
    latitude=models.FloatField(null=True , blank=True)

    