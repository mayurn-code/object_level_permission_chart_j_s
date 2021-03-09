# from rest_framework import routers
from django.urls import path, include
from .views import homepage,ListView


urlpatterns = [
    path('',homepage,name='homepage'),
    path('api/',ListView.as_view(),name='listview'),
]