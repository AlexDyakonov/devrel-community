from rest_framework import serializers
from .models import Event, FormFields
from users.serializers import UserSerializer
from users.models import User

class EventSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    participants = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = (
            'id', 'title', 'speakers', 'banner', 'description', 'event_type', 'location', 'participants', 'start_time',
            'end_time',
            'social_media_link')
    
    def get_banner_url(self, obj):
        return obj.get_banner_url()

    def create(self, validated_data):
        participants_data = validated_data.pop('participants', [])

        event = Event.objects.create(**validated_data)

        for participant_data in participants_data:
            user, created = User.objects.get_or_create(**participant_data)
            event.participants.add(user)

        return event


class FormFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFields
        fields = '__all__'
