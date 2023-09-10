from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from telegram_bot.models import TelegramMessage

from .permissions import IsChatID
from .serializers import (SignUpSerializer, TelegramListMessagesSerializer,
                          TelegramMessageSerializer, UserProfileSerializer)
from .services import create_and_send_telegram_message

CustomUser = get_user_model()


class SignUpCreateAPIView(CreateAPIView):
    """
    API view for user registration (sign-up).

    This view allows any user, authenticated or not, to register (sign up) by providing their
    'name', 'username', and 'password' through the API.

    Attributes:
        serializer_class (Serializer): The serializer class to use for user registration.
        permission_classes (tuple): The permissions required to access this view, allowing any user to register.

    """
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny, )


class TelegramMessagesListAPIView(ListAPIView):
    """
    API view for listing Telegram messages.

    This view allows authenticated users to retrieve a list of their own Telegram messages.

    Attributes:
        serializer_class (Serializer): The serializer class to use for message serialization.

    Methods:
        get_queryset(self): Get the queryset of Telegram messages for the current user.

    """
    serializer_class = TelegramListMessagesSerializer

    def get_queryset(self):
        """
        Get the queryset of Telegram messages for the current user.

        Returns:
            QuerySet: The queryset containing Telegram messages of the current user.

        """
        return TelegramMessage.objects.filter(user_id=self.request.user.id)


class TelegramMessageCreateAPIView(CreateAPIView):
    """
    API view for creating Telegram messages.

    This view allows authenticated users with a chat_id to create Telegram messages.
    The created message is then sent as a notification to the user's Telegram chat.

    Attributes:
        serializer_class (Serializer): The serializer class to use for message creation.
        permission_classes (tuple): The permissions required to access this view.

    Methods:
        post(self, request, *args, **kwargs): Create a Telegram message and send it as a notification.

    """
    serializer_class = TelegramMessageSerializer
    permission_classes = (IsAuthenticated, IsChatID)

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Create a Telegram message and send it as a notification.

        Args:
            request (Request): The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: HTTP response indicating the result of the message creation.

        """
        response = self.create(request, *args, **kwargs)
        create_and_send_telegram_message(request)
        return response


class UserProfileAPIView(RetrieveAPIView):
    """
    API view for retrieving a user's profile by their unique slug.

    This view allows retrieving a user's profile by specifying their unique slug as part of the URL.
    The user's profile information, including their name, username, and other details, is serialized using the
    UserProfileSerializer.

    Attributes:
        serializer_class (Serializer): The serializer class used to serialize the user's profile data.
        queryset (QuerySet): The queryset used to retrieve user profiles.
        lookup_field (str): The field to use as the lookup parameter for retrieving user profiles by slug.

    """
    serializer_class = UserProfileSerializer
    queryset = CustomUser
    lookup_field = 'slug'
