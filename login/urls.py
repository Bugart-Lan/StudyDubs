from django.urls import path

from . import views

urlpatterns = [
  path("", views.getLogin, name = "login"),
  path("register/", views.getRegister, name = "register"),
  path("success/", views.success, name = "success")
]