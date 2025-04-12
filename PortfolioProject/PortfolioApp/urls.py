from django.contrib import admin
from django.urls import path
from .views import PortfolioDetailsView, UserRegister, UserLogin

urlpatterns = [
    path('portfolio/', PortfolioDetailsView.as_view()),
    path('portfolio/<str:email>/', PortfolioDetailsView.as_view()),
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view())
]

