from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.join),
    path('login/', views.login),
    path('mypage/', views.mypage),
]
