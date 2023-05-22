from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUserForm

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('chat:mypage')

class UserLogoutView(LogoutView):
    template_name = 'logout.html'

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CreateUserForm
    
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response