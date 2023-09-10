from django.contrib.auth import get_user_model

CustomUser = get_user_model()


def assign_chat_id_by_token(message_text: str, chat_id: int) -> bool:
    """
    Assign the chat_id to a user based on their Telegram token.

    Args:
        message_text (str): The Telegram token provided in the message.
        chat_id (int): The chat_id to update.

    Returns:
        bool: True if the chat_id was updated, False otherwise.
    """
    updated_count = CustomUser.objects.filter(
        token_telegram=message_text).update(chat_id=chat_id)
    return bool(updated_count)


def get_custom_user_by_chat_id(chat_id: int) -> CustomUser | None:
    """
    Get a CustomUser object by its chat_id.

    Args:
        chat_id (int): The chat_id of the user.

    Returns:
        CustomUser | None: The CustomUser object or None if not found.
    """
    try:
        custom_user = CustomUser.objects.get(chat_id=chat_id)
        return custom_user
    except CustomUser.DoesNotExist:
        return None


def process_telegram_message(chat_id: int, message_text: str) -> str:
    """
    Process an incoming Telegram message and return a response text.

    Args:
        chat_id (int): The ID of the Telegram chat.
        message_text (str): The text of the incoming message.

    Returns:
        str: The response text to send back to the user.
    """
    custom_user = get_custom_user_by_chat_id(chat_id)

    if custom_user is None:
        updated_count = assign_chat_id_by_token(message_text, chat_id)
        if not updated_count:
            response_text = 'Register on the website ... and get a token, then write it here to link the bot to the site'
        else:
            response_text = 'Chat ID updated successfully.'
    else:
        response_text = 'You have already been authorized and can send yourself messages on Telegram'

    return response_text
