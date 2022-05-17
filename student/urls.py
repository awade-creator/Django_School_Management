from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import student_profile, student_dashboard

app_name = "student"
urlpatterns = [
    path("", views.home, name="home"),
    path("student_profile/", student_profile, name="student_profile"),
    path("student_dashboard/", student_dashboard, name="student_dashboard"),
]
