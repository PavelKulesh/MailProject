from django.shortcuts import render


def home(request):
    return render(request, 'login/home.html')


def sign_in(request):
    return render(request, 'login/sign_in.html')


def sign_up(request):
    return render(request, 'login/sign_up.html')
