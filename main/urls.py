from django.contrib.auth import views as auth_views
from main import views as user_views
from django.urls import path, include
from . import views
from .views import register

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="main/login.html")),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]
