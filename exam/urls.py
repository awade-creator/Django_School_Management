from django.urls import path
from . import views
from .views import exam_create

app_name = "exam"
urlpatterns = [
    path("", views.home, name="home"),
    path('exam_create/<int:pk>/', views.exam_create, name='exam_create'),
    path('exam/<slug:slug>/', views.exam_detail_view, name='exam-detail'),
]
