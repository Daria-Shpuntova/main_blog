from django.urls import path
from . import views

urlpatterns = [
    path('homemarket/', views.Home.as_view(), name='homemarket'),
    path('all_courses/', views.CoursesHomePage.as_view(), name='homecourses'),
    path('course/<slug>', views.CoursePage.as_view(), name='course_page'),
    path('course/<slug>/<les_slug>', views.LessonPage.as_view(), name='les_page'),
    path('articles/', views.ArticlesList.as_view(), name='articles'),
    path('articles/<int:art_id>/', views.art, name='art_id'),
    path('cat/<slug:cat_slug>/', views.Courses_slag.as_view(), name='cat_slug'),
]
