from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
    template_name = 'index.html'


class LoginPage(TemplateView):
    template_name = 'loginview.html'

class LogoutPage(TemplateView):
    template_name = 'logoutview.html'
