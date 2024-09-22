from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    '''User Serializer to return json'''
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'code', 'password']