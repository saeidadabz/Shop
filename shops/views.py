
from .models import Shop
from .serializer import ShopCreateSerializer , ShopRetrieveSerializer,ShopUpdateSerializer
# Create your views here.


from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , RetrieveAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError

from drf_spectacular.utils import extend_schema


class CreateShopView(CreateAPIView):
    queryset=Shop.objects.all()
    serializer_class=ShopCreateSerializer
    permission_classes=[IsAuthenticated]

  
    def perform_create(self, serializer):
       
       #user must have just 1 shop
       if Shop.objects.filter(user=self.request.user).exists():
           raise ValidationError({"error":"you already have a shop and cannot create another one"})

       #for complete user field in shop table
       serializer.save(user=self.request.user)
    

class ShopDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Shop.objects.all()
    
    #permission_classes=[]


    #when i want retrieve a shop we need that vendor  but when we want update shop we dont need vendor detail in response
    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH']:
            return ShopUpdateSerializer
        return ShopRetrieveSerializer
    
  




# class CreateShopView(APIView):
   
#     @extend_schema(
#         request=ShopCreateSerializer,
#         responses=ShopCreateSerializer
#     )

#     def post(self,request):

#         serializer=ShopCreateSerializer(data=request.data, context={'request':request})
       
#         if serializer.is_valid():
#             shop=serializer.save()
#             print(shop)

#             return Response(serializer.data,200)

        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      



