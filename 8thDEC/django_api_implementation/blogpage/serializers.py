from rest_framework import serializers 
from .models import players 
# need to install from here https://www.django-rest-framework.org/ # this file is for converting into json 
class playerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = players 
        fields = {'fname', 'lname', 'playerType', 'jerseyNumber'} 
        fields = '__all__' 