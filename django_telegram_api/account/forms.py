from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new custom user accounts.

    This form extends the built-in UserCreationForm provided by Django
    to include the 'name' field in addition to the 'username' and password fields.

    Attributes:
        model (Model): The model class to use for creating the user account.
        fields (tuple): The fields to include in the form.

    """
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'password1', 'password2')
