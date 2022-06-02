from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Email


class InboxList(LoginRequiredMixin, ListView):
    model = Email
    context_object_name = 'emails'
    template_name = 'main/inbox_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = context['emails'].filter(recipient=self.request.user, is_deleted=False)
        return context


class SentList(LoginRequiredMixin, ListView):
    model = Email
    context_object_name = 'emails'
    template_name = 'main/sent_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = context['emails'].filter(sender=self.request.user)
        return context


class EmailDetail(LoginRequiredMixin, DetailView):
    model = Email
    context_object_name = 'email'
    template_name = 'main/email.html'


class EmailCreate(LoginRequiredMixin, CreateView):
    model = Email
    fields = ['recipient', 'topic', 'text']
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(EmailCreate, self).form_valid(form)


class EmailDelete(LoginRequiredMixin, DeleteView):
    model = Email
    context_object_name = 'email'
    success_url = reverse_lazy('inbox')
