from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("survey", views.survey, name="survey"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("create_account", views.create_account, name="create_account"),
    path("getSchedule", views.getSchedule, name="getSchedule"),
    path("common_time", views.showCommonTime, name="common_time")
]
