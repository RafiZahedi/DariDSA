from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson_list, name='lesson_list'),
    path('feedback/', views.feedback, name='feedback'),
    path('<slug:slug>/', views.lesson_detail, name='lesson_detail'),
    
]
