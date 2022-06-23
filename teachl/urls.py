from django.urls import path,include
from .views import *


urlpatterns = [
    path('',teacp,name="my-view"),
    path('m/logout',logout,name="logout"),
    path('c/logout',logout,name="logout"),
    path('p/logout',logout,name="logout"),
    path('create',createclass_form),
    path('createc',createclass),
    path('c/<str:cod>/',classpass),
    path('c/<str:cod>/',classwork),
    path('p/<str:cod>/',prople),

    path('c/<str:cod>/<str:tcod>/add',uploader),
    path('c/<str:cod>/<str:tcod>/<str:pdfcode>/addmark',markupdate),
    path('c/<str:cod>/tadder',topicadder),
    path('c/<str:cod>/addassigment',addassgment),
    path('callback',callback),
    path("p/<str:cod>/addstd",addstd),
    #path('m/<str:cod>/delete',deletedrivefile),
]