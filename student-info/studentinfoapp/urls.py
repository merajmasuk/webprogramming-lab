from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
]