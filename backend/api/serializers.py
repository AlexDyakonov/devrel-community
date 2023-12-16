from rest_framework import serializers
from .models import Event, FormFields

class EventSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Event
        fields = ['id', 'title', 'speakers', 'banner', 'description', 'event_type', 'location', 'start_time', 'end_time', 'social_media_link']

    def get_banner_url(self, obj):
        return obj.get_banner_url()
    
class FormFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFields
        fields = '__all__'
