from rest_framework import serializers
from telegram_bot.models import TelegramMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

CustomUser = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'token_telegram')


class TelegramMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a Telegram message.

    This serializer is used for creating Telegram messages, and it includes the 'message_text' field.
    The 'user_id' field is automatically set to the currently authenticated user.

    Attributes:
        user_id (int): The ID of the authenticated user.

    """
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta():
        model = TelegramMessage
        fields = ('message_text', 'user_id')


class TelegramListMessagesSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Telegram messages.

    This serializer is used for listing Telegram messages and includes the 'dispatch_date' and 'message_text' fields.

    Attributes:
        None

    """
    class Meta():
        model = TelegramMessage
        fields = ('dispatch_date', 'message_text')


class SignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.

    This serializer is used for serializing the CustomUser model, including the 'name', 'username', and 'password' fields.
    The 'password' field is marked as write-only.

    Attributes:
        None

    """
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> CustomUser:
        """
        Create a new CustomUser instance with the provided validated data.

        Args:
            validated_data (dict): Validated data for creating the user.

        Returns:
            CustomUser: The created CustomUser instance.

        """
        user = CustomUser.objects.create(
            username=validated_data['username'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_password(self, password: str) -> str:
        """
        Validate the password using Django's built-in password validation.

        Args:
            value (str): The password value to validate.

        Returns:
            str: The validated password.

        Raises:
            serializers.ValidationError: If the password does not meet the validation criteria.
        """
        validate_password(password)
        return password
