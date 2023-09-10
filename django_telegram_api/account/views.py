from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

CustomUser = get_user_model()


class HomePageView(TemplateView):
    """
    View for displaying the home page.

    This view renders the 'account/index.html' template as the home page.

    Attributes:
        template_name (str): The name of the template to render for the home page.

    """
    template_name = 'account/index.html'


class SignUpCreateView(CreateView):
    """
    View for user registration.

    This view uses the CustomUserCreationForm to handle user registration.
    Upon successful registration, users are redirected to the home page.

    Attributes:
        form_class (Form): The form class to use for user registration.
        template_name (str): The name of the template to render for the registration page.
        success_url (str): The URL to redirect to after successful registration.

    """
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home-url')


class ProfilePageView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the user's profile page.

    This view requires users to be logged in. It renders the 'account/profile.html' template.

    Attributes:
        template_name (str): The name of the template to render for the profile page.
        login_url (str): The URL to redirect unauthenticated users to for login.

    """
    template_name = 'account/profile.html'
    login_url = reverse_lazy('login')
