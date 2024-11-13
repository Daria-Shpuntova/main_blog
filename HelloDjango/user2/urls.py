"""
URL configuration for webblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user2 import views as userViews
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reg/', userViews.register, name='reg'),
    path('user/', authViews.LoginView.as_view(template_name='user2/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='user2/exit.html'), name='exit'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='user2/pass-reset.html'), name='pass-reset'),
    path('pass-reset_complite/', authViews.PasswordResetCompleteView.as_view(template_name='user2/pass-reset_complite.html'), name='pass-reset_complite'),
    path('password_reset_confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='user2/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done/<uidb64>/<token>/',
         authViews.PasswordResetDoneView.as_view(template_name='user2/password_reset_done.html'),
         name='password_reset_done'),
    path('profile/', userViews.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)