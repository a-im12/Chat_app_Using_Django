from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('mypage/', views.MyPageView.as_view(), name='mypage'),
]