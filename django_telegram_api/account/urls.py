from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-url'),
    path('sign-up/', views.SignUpCreateView.as_view(), name='sign-up-url'),
    path('user/<slug:slug_user>/',
         views.ProfilePageView.as_view(), name='profile-url'),
]
