from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['name', 'age', 'gender', 'is_present', 'street', 'city', 'state', 'postal_code']

    
