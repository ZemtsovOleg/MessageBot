from django.conf import settings
from django.urls import path

from .views import TelegramMessageAPIView

urlpatterns = [
    path(f'{settings.API_TOKEN}/message/',
         TelegramMessageAPIView.as_view()),
]
