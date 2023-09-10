import secrets

from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

validate_slug.message = _(
    "Enter a valid value consisting of letters, numbers, underscores, or hyphens."
)


class CustomUser(AbstractUser):
    """
    Custom user model for your application.

    This model extends the built-in AbstractUser model and includes additional
    fields like 'name', 'slug', 'token_telegram', and 'chat_id'.

    Attributes:
        username (str): The unique username for the user.
        name (str): The user's name.
        slug (str): The slugified version of the username.
        token_telegram (str): The Telegram token associated with the user.
        chat_id (str): The chat ID associated with the user.

    Methods:
        save(self, *args, **kwargs): Custom save method to generate a unique token and slug.
        get_absolute_url(self): Get the absolute URL for the user's profile.
        __str__(self): Return a string representation of the user.
        generate_unique_token() -> str: Generate a unique Telegram token for the user.
    """
    username = models.CharField(
        _("username"),
        max_length=255,
        unique=True,
        help_text=_(
            "Required. 255 characters or fewer. Letters, digits and -/_ only."
        ),
        validators=(validate_slug, ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    token_telegram = models.CharField(max_length=255, unique=True)
    chat_id = models.CharField(max_length=255, unique=True, null=True)

    def save(self, *args, **kwargs):
        """
        Save method to generate a unique token and slug.

        If the 'token_telegram' field is not set, a unique Telegram token
        will be generated. Additionally, the 'slug' field is generated based on
        the 'username' field.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            None

        """
        if not self.token_telegram:
            self.token_telegram = self.generate_unique_token()
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the absolute URL for the user's profile.

        Returns:
            str: The absolute URL for the user's profile.

        """
        return reverse_lazy('profile-url', args=(self.slug, ))

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
            str: The string representation of the user.

        """
        return str(self.username)

    def generate_unique_token(self) -> str:
        """
        Generate a unique Telegram token for the user.

        Args:
            token_length (int): The length of the generated token (default is 16).

        Returns:
            str: A unique Telegram token.

        """
        while True:
            new_token = secrets.token_hex(16)
            if not CustomUser.objects.filter(token_telegram=new_token).exists():
                return new_token
