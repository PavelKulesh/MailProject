from django.urls import path
from .views import LoginPage, RegisterPage, home

urlpatterns = [
    path('', home, name='home'),
    path('sign-in/', LoginPage.as_view(), name='sign-in'),
    path('sign-up/', RegisterPage.as_view(), name='sign-up'),
]
