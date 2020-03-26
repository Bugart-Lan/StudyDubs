from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("schedule", views.schedule, name="schedule"),
    path("survey", views.survey, name="survey"),
    path("getSurveyResults", views.getSurveyResults, name="getSurveyResults"),
    path("login_page", views.login, name="login"),
    path("login_view", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("create_account", views.create_account, name="create_account"),
    path("getSchedule", views.getSchedule, name="getSchedule"),
    path("common_time", views.showCommonTime, name="common_time")
]
