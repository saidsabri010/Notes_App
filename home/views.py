from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.


class LoginInterfaceView(LoginView):
    template_name = 'login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super().get(request, *args, **kwargs)


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'


def index(request):
    return render(request, "base.html")


@login_required(login_url='admin/')
def authorized(request):
    return render(request, 'authorized.html', {})
