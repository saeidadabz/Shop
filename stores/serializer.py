

from rest_framework import serializers
from .models import Store
from drf_spectacular.utils import extend_schema_field

# from users.serializer import CustomerRegisterSerializer
from vendors.serializer import VendorSerializer

from Shop import settings


class StoreCreateSerializer(serializers.ModelSerializer):

    

        class Meta:
            model=Store

            fields=['store_name','store_address','longitude']
            extra_kwargs={
                 'store_address':{'required':True}
            }

        # i handle this  in perform_create() method in CreateShopView class

        # def create(self, validated_data):
        #     # گرفتن کاربر از request
        #     user = self.context['request'].user
        #     validated_data['user'] = user  # اختصاص کاربر به فروشگاه
        #     return super().create(validated_data)

class StoreRetrieveSerializer(serializers.ModelSerializer):

        user=VendorSerializer()

        class Meta:
            model=Store
            fields=['id','store_name','store_address','longitude','user']

class StoreUpdateSerializer(serializers.ModelSerializer):
      
      class Meta:
            model=Store
            fields=['id','store_name','store_address','longitude']

            
        
        

         