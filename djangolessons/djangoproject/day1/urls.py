from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateStudent, name='create_student'),
    path('std_detail/<str:reg>/', views.GetStudent, name='std_detail'),
    path('delete/<str:id>', views.DeleteStudent, name='delete'),
    path('update/<str:id>', views.UpdateStudent, name='update'),
