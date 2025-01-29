from django.urls import path

from .views import StoreCreateView,StoreListView,StoreDetailApiView


urlpatterns=[
    path('store/create',StoreCreateView.as_view()),
    path('store/',StoreListView.as_view()),
    path('store/<int:pk>/',StoreDetailApiView.as_view()),


  
]
