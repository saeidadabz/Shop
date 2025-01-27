from django.urls import path

from .views import CustomerRegisterView

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns=[
    #behtar nis bezarim hamun 'register/' ?
    path('customer/register/',CustomerRegisterView.as_view()),
    # path('VendorRegister'),
    # path('DriverRegister'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify')
]
