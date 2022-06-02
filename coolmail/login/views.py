from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


def home(request):
    if request.user.is_authenticated:
        return redirect('inbox')
    else:
        return render(request, 'login/home.html')


class LoginPage(LoginView):
    template_name = 'login/sign_in.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        return render(self.request, 'login/sign_in_error.html')

    def get_success_url(self):
        return reverse_lazy('inbox')


class RegisterPage(FormView):
    template_name = 'login/sign_up.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inbox')
        return super(RegisterPage, self).get(*args, **kwargs)

    def form_invalid(self, form):
        return render(self.request, 'login/sign_up_error.html')
