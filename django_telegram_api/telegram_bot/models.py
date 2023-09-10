from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

CustomUser = get_user_model()


class TelegramMessage(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    message_text = models.TextField(blank=True)
    dispatch_date = models.DateTimeField(
        _('dispatch date'), default=timezone.now)

    def __str__(self) -> str:
        return str(self.message_text)
