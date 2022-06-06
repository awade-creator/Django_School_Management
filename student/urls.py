from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import student_profile, student_dashboard, exam_report_view, exam_create

app_name = "student"
urlpatterns = [
    path("", views.home, name="home"),
    path("student_profile/", student_profile, name="student_profile"),
    path("student_dashboard/", student_dashboard, name="student_dashboard"),
    path('exam_create/<str:pk_exam>', exam_create, name='exam_create'),
    path("exam_report_view/", views.exam_report_view, name="exam_report_view"),
]
