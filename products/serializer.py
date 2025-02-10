from rest_framework import serializers
from .models import Product

from stores.serializer import StoreRetrieveSerializer

class ProductCreateSerializer(serializers.ModelSerializer):

     
      class Meta:
            model=Product
           

            fields = '__all__'
            read_only_fields = ['store', 'created_at'] 

class ProductDetailSerializer(serializers.ModelSerializer):
      store=StoreRetrieveSerializer()
      class Meta:
            model=Product
      
            fields = '__all__'
            read_only_fields = ['store', 'created_at'] 

            
