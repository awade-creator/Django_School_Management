import django.views.generic
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
from .views import student_profile, student_dashboard, exam_list, exam_create

app_name = "student"
urlpatterns = [
    path("", views.home, name="home"),
    path("student_profile/", student_profile, name="student_profile"),
    path("student_dashboard/", student_dashboard, name="student_dashboard"),
    path('exam_create/<str:pk_exam>', exam_create, name='exam_create'),
    # path("exam_list", login_required(TemplateView.as_view)),
    path("exam_list", exam_list.as_view(), name='exam_list'),
]
