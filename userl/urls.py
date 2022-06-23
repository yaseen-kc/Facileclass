from django.urls import path,include
from .views import *


urlpatterns = [
    path('',userp),
    path('logout',logout,name="logout"),
    path('create',createclass_form),
    path('createc',createclass),
    path('c/<str:cod>/',classwork),
    path('p/<str:cod>/',prople),
    path('c/<str:cod>/',classwork),
    path('scallback',callback),
    path('c/<str:cod>/<str:tcod>/addassigment',uploader),
]