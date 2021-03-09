from django.shortcuts import render
from rest_framework import generics
from .serializers import TagSerializer
from .models import Tag_C8738A28CFF7
from datetime import datetime, timedelta
from django.utils import timezone

"""
this is Showing Home Page
"""
def homepage(request):
    return render(request,'index.html')

class ListView(generics.ListAPIView):
    queryset = Tag_C8738A28CFF7.objects.all().order_by('-date_time')
    serializer_class = TagSerializer
    
    # today = datetime.datetime.today()
    # queryset = Tag_C8738A28CFF7.objects.all()
    # now = datetime.datetime.now()
    # four_hour = now -datetime.timedelta(hours=4)
    # queryset = Tag_C8738A28CFF7.filter(date_time__range=[datetime.datetime(four_hour),datetime.datetime(now)])
    # queryset = Tag_C8738A28CFF7.objects.filter(date_time__range=[timezone.now(),datetime.timedelta(hours=4)])    
    # print('------',queryset)

# class Want7daysData(viewsets.ModelViewSet):
    # queryset = Tag_C8738A28CFF7.objects.filter(date_time__range=[datetime.datetime(2020,10,14),datetime.datetime(2020,10,26)])
    # print(today)
    