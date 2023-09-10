from rest_framework.request import Request

from telegram_bot.telegram_api import send_telegram_notification


def format_message(username: str, message_text: str) -> str:
    """
    Format a notification message.

    Args:
        username (str): The username to include in the message.
        message_text (str): The text of the message.

    Returns:
        str: The formatted message.

    """
    return f"{username}, я получил от тебя сообщение:\n{message_text}"


def create_and_send_telegram_message(request: Request) -> None:
    """
    Create a Telegram message and send it as a notification.

    Args:
        request (Request): The HTTP request object containing user and message information.

    Returns:
        None
    """
    chat_id = request.user.chat_id
    message_text = request.data['message_text']
    formatted_message = format_message(request.user.name, message_text)
    send_telegram_notification(chat_id, formatted_message)
    return None
