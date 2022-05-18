from main import views as user_views
from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', user_views.profile, name='profile'),
]
