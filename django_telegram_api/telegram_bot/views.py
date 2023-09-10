from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import process_telegram_message
from .telegram_api import send_telegram_notification


class TelegramMessageAPIView(APIView):
    """
    API view for handling incoming messages from Telegram.
    """
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        """
        Handle a POST request with incoming Telegram messages.

        Args:
            request (Request): The incoming HTTP request.

        Returns:
            Response: The HTTP response indicating the result.
        """
        chat_id: int = request.data['message']['chat']['id']
        message_text: str = request.data['message']['text']

        response_text = process_telegram_message(chat_id, message_text)
        send_telegram_notification(chat_id, response_text)

        return Response({"message": "Message received"})
