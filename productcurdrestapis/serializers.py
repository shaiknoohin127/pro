from rest_framework import serializers 
from productcurdrestapis.models import *


class productSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Product
        fields = '__all__'