from django.urls import path
from .views import InboxList, SentList, EmailDetail, EmailCreate, EmailDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inbox/', InboxList.as_view(), name='inbox'),
    path('sent/', SentList.as_view(), name='sent'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('email/<int:pk>/', EmailDetail.as_view(), name='email'),
    path('email-create/', EmailCreate.as_view(), name='email-create'),
    # path('email-update/<int:pk>/', EmailUpdate(), name='email-update'),
    path('email-delete/<int:pk>/', EmailDelete.as_view(), name='email-delete'),
]
