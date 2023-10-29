from django.urls import path, re_path, include
from account import views

urlpatterns = [
    path('register/', views.RegisterEmployee.as_view(), name="register")
]
