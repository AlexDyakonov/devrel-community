from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .tasks import bar, send_mailing, send_tg_message
from .serializers import MailingSerializer, MailSerializer, TgMessageSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class TestWorker(APIView):
    @staticmethod
    def post(request):
        bar.delay()
        return Response("succeed")


class MailingView(CreateAPIView):
    serializer_class = MailingSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            emails: list = serializer.validated_data.get('emails')
            mail: MailSerializer = serializer.validated_data.get('mail')

            send_mailing.delay(emails, mail)

            return Response({'success': True}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class TgMessageView(CreateAPIView):
    serializer_class = TgMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = TgMessageSerializer(data=request.data)
        if serializer.is_valid():
            tg_ids = serializer.validated_data.get('tg_ids')
            message = serializer.validated_data.get('message')

            send_tg_message.delay(tg_ids, message)

            return Response({'success': True}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)