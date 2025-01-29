
from .models import Store
from .serializer import StoreCreateSerializer , StoreRetrieveSerializer,StoreUpdateSerializer
# Create your views here.


from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response  
from rest_framework.permissions import IsAuthenticated
from .permissions import IsVendor , IsOwner
from rest_framework import status
from rest_framework.exceptions import ValidationError

from drf_spectacular.utils import extend_schema


class StoreCreateView(CreateAPIView):
    queryset=Store.objects.all()
    serializer_class=StoreCreateSerializer
    permission_classes=[IsAuthenticated,IsVendor]

  
    def perform_create(self, serializer):
       
       #user must have just 1 store
       if Store.objects.filter(user=self.request.user).exists():
           raise ValidationError({"error":"you already have a store and cannot create another one"})

       #for complete user field in store table
       serializer.save(user=self.request.user)
    
class StoreListView(ListAPIView):
    queryset=Store.objects.all()
    serializer_class=StoreRetrieveSerializer
    # permission_classes=[IsAuthenticated,IsVendor]


class StoreDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Store.objects.all()
    
    permission_classes=[IsOwner]

    #when i want retrieve a store we need that vendor  but when we want update store we dont need vendor detail in response
    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH']:
            return StoreUpdateSerializer
        return StoreRetrieveSerializer
    
  




# class CreatestoreView(APIView):
   
#     @extend_schema(
#         request=storeCreateSerializer,
#         responses=storeCreateSerializer
#     )

#     def post(self,request):

#         serializer=storeCreateSerializer(data=request.data, context={'request':request})
       
#         if serializer.is_valid():
#             store=serializer.save()
#             print(store)

#             return Response(serializer.data,200)

        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      



