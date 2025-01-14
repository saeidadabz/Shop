from django.urls import path

from .views import CreateShopView,ShopDetailApiView


urlpatterns=[
    path('shop/create',CreateShopView.as_view()),
    path('shop/<int:pk>/',ShopDetailApiView.as_view()),


  
]
