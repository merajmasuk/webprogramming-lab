from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('insert/', views.insert, name="insert"),
    path('view_student/', views.view_student, name="view"),
    path('view_student/<int:student_id>', views.view_student, name="view"),
]