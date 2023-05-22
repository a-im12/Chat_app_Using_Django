from django.shortcuts import render
from django.views.generic import TemplateView

class MyPageView(TemplateView):
    template_name = 'mypage.html'