from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.exceptions import PermissionDenied , ValidationError

from .models import Product
from .serializer import ProductCreateSerializer, ProductDetailSerializer
from .permissions import IsOwner, IsVendor
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # serializer_class = ProductSerializer
    permission_classes=[IsOwner,IsVendor]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:  # اگر درخواست GET باشد
            return ProductDetailSerializer
        return ProductCreateSerializer 

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'Vendor':
            raise PermissionDenied("این کاربر فروشنده نیست و نمی‌تواند محصول اضافه کند.")
        
        if not  hasattr(user,'store'):
            raise ValidationError({"error": "برای ثبت محصول ابتدا باید یک فروشگاه ایجاد کنید."})
            
            # ذخیره محصول با مقداردهی shop
        serializer.save(store=user.store)


