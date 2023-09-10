from django.urls import path

from . import views


urlpatterns = [
    path('sign-up/', views.SignUpCreateAPIView.as_view()),
    path('user/<slug:slug>/', views.UserProfileAPIView.as_view()),
    path('create_message/', views.TelegramMessageCreateAPIView.as_view()),
    path('list_messages/', views.TelegramMessagesListAPIView.as_view()),
]
