from rest_framework import serializers
from .models import Tag_C8738A28CFF7

class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Tag_C8738A28CFF7
        fields = ['id','date_time','temperature','humidity']

