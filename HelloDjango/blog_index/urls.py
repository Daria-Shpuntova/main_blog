from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('works/', views.Works.as_view(), name='works'),
    path('progect/<int:prog_id>/', views.Progect_page.as_view(), name='prog_id'),
    path('tag/<int:tag_id>/', views.Tag_id.as_view(), name='tag_id'),
]