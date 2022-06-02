from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'member'
urlpatterns = [
    path('register_user/',
         views.register_user,
         name='register_user'),
    path('login/',
         auth_views.LoginView.as_view(template_name='member/authentication/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='member/authentication/logout.html'),
         name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='member/authentication/password_change.html'),
         name='password_change'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='member/authentication/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='member/authentication/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name='member/authentication/password_reset_done.html'),
         name='password_reset_done'),
]
