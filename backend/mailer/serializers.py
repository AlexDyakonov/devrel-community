from rest_framework import serializers


class MailSerializer(serializers.Serializer):
    text = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()
    html_message = serializers.CharField()


class MailingSerializer(serializers.Serializer):
    emails = serializers.ListField(child=serializers.EmailField(), required=True)
    mail = MailSerializer(required=True)


class TgIdListSerializer(serializers.Serializer):
    tg_ids = serializers.ListField(child=serializers.IntegerField(), required=True)

class TgMessageSerializer(serializers.Serializer):
    tg_ids = serializers.ListField(child=serializers.IntegerField(), required=True)
    message = serializers.CharField(required=True)