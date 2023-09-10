from django.contrib import admin

from .models import TelegramMessage


@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    pass
