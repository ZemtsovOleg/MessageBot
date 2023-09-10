import requests
from django.conf import settings


def send_telegram_notification(chat_id: int, text: str) -> None:
    """
    Sends a notification to a Telegram chat.

    Args:
        chat_id (int): The ID of the Telegram chat.
        text (str): The text of the notification.

    Returns:
        None
    """
    telegram_url = f'{settings.TELEGRAM_URL}sendMessage'
    response = {'chat_id': chat_id, 'text': text}
    requests.post(telegram_url, json=response)
    return None
