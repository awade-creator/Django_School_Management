from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='member/authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='member/authentication/logout.html'),
         name='logout'),
    path('register_user/', views.register_user, name='register_user'),
]
