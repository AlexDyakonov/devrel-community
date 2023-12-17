from rest_framework import serializers
from .models import Source, SourceUsers

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class SourceUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceUsers
        fields = '__all__'
