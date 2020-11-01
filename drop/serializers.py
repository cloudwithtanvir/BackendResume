from rest_framework import serializers
from .models import Drop


class DropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drop
        fields = ('id', 'name', 'email', 'phone_number','tech_expert' ,'upload', 'comments', 'position', 'heard','created_at')
