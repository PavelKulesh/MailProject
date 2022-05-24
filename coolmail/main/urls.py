from django.urls import path
from . import views

urlpatterns = [
    path('inbox', views.inbox, name='inbox'),
    path('sent', views.sent, name='sent'),
    path('trash', views.trash, name='trash'),
    path('search', views.search, name='search'),
    path('write', views.write, name='write'),
]
