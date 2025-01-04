
from rest_framework import serializers
from .models import User
from drf_spectacular.utils import extend_schema_field

from Shop import settings


class VendorRegisterSerializer(serializers.ModelSerializer):


        class Meta:
            model=User
            fields=['email','mobile','password','token','role']
            extra_kwargs={
                 'mobile':{'required':True},
                 'role':{'read_only':True}
            }
        

        token=serializers.SerializerMethodField('get_token')

        @extend_schema_field(str)
        def get_token(self,obj):
          return self.context.get('token')

            
        
        def create(self, validated_data):
        
            user=User.objects.create_user(
                 email=validated_data['email'],
                 mobile=validated_data['mobile'],
                 password=validated_data['password'],
                 role=settings.ROLE_CHOICES['vendor']
            
            )

            return user