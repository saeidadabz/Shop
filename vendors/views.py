from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from .serializer import VendorRegisterSerializer

from drf_spectacular.utils import extend_schema
# Create your views here.





#vendor register

class VendorRegisterView(APIView):

    @extend_schema(
        request=VendorRegisterSerializer,
        responses={201: VendorRegisterSerializer},
    )
    def post(self,request):
        
        email=request.data.get('email')

        if User.objects.filter(email=email).exists():
            return Response({'detaail':'user alreaaady registered'})


        serializer=VendorRegisterSerializer(data=request.data)

       


        if serializer.is_valid():
          
            user= serializer.save()
            print(user)

            # print(type(user))

            refresh=RefreshToken.for_user(user)
            access_token=refresh.access_token
            
            token={
                "refresh":str(refresh),
                "access_token":str(access_token)
            }
            user_serializer= VendorRegisterSerializer(user,context={'token':token})
           
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# create vendor store

class CreateVendorInfo(APIView):
    def post(seld,request):
        pass


#تغییر پروفایل


#لیست همه فروشگاه ها

    # better move to shop