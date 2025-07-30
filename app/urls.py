from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_list, name='students_list'),
    path('students/<int:pk>/', views.students_detail, name='students_detail'),
]
