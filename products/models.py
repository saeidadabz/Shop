from django.db import models
from stores.models import Store
# Create your models here.

class Product (models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
    price=models.DecimalField(max_digits=12,decimal_places=0)
    quantity=models.IntegerField()
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد محصول
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ آخرین بروزرسان
