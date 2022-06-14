from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Email
import logging
from .tasks import email_created


logger = logging.getLogger('django')


class InboxList(LoginRequiredMixin, ListView):
    """This class allows you to interact with the list of incoming emails"""
    model = Email
    context_object_name = 'emails'
    template_name = 'main/inbox_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = context['emails'].filter(recipient=self.request.user, is_deleted=False)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['emails'] = context['emails'].filter(topic__startswith=search_input)
        context['search_input'] = search_input
        return context


class SentList(LoginRequiredMixin, ListView):
    """This class allows you to interact with the list of sent emails"""
    model = Email
    context_object_name = 'emails'
    template_name = 'main/sent_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = context['emails'].filter(sender=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['emails'] = context['emails'].filter(topic__startswith=search_input)
        context['search_input'] = search_input
        return context


class EmailDetail(LoginRequiredMixin, DetailView):
    """This class allows you to interact with a specific email"""
    model = Email
    context_object_name = 'email'
    template_name = 'main/email.html'


class EmailCreate(LoginRequiredMixin, CreateView):
    """This class allows you to create an email"""
    model = Email
    fields = ['recipient', 'topic', 'text']
    success_url = reverse_lazy('inbox')
    logger.info('Email was created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = User.objects.all()
        return {'users': context}

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(EmailCreate, self).form_valid(form)

    email_created.delay(model.id)


class EmailDelete(LoginRequiredMixin, DeleteView):
    """This class allows you to delete an email"""
    model = Email
    context_object_name = 'email'
    success_url = reverse_lazy('inbox')
    logger.info('Email was deleted')
