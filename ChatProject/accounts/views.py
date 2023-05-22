from django.shortcuts import render
from django.views.generic import TemplateView

class UserLoginView(TemplateView):
    template_name = 'login.html'
