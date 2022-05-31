from django.shortcuts import render
from .models import Emails


def inbox(request):
    emails = Emails.objects.all()
    return render(request, 'main/inbox.html', {'emails': emails})


def sent(request):
    return render(request, 'main/sent.html')


def trash(request):
    return render(request, 'main/trash.html')


def search(request):
    return render(request, 'main/search.html')


def write(request):
    return render(request, 'main/write.html')
