from django.urls import path

from . import views

urlpatterns = [
  path("", views.getLogin, name = "login"),
  path("loginUser/", views.loginUser, name = "loginUser"),
  path("register/", views.getRegister, name = "register"),
  path("registerUser", views.registerUser, name = "registerUser"),
  path("success/", views.success, name = "success")
]