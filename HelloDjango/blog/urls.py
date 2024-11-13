from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='homeblog'),
    path('user/<str:username>', views.UserNewsView.as_view(), name='user-news'),
    path('news/<int:pk>', views.NewsDetaliView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.UpdateNewsVies.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='delete-news'),
    path('news/add', views.CreateNewsVies.as_view(), name='news-add'),
    path('about', views.about, name='about'),
    path('cont', views.contacts, name='cont'),
]
