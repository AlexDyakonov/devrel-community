from rest_framework import serializers

from .models import ReffLink


class ReffLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReffLink
        fields = '__all__'
