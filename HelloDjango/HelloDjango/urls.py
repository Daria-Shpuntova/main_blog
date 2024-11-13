from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_index.urls')),
    path('courses/', include('courses.urls')),
    path('user1/', include('user1.urls')),
    path('blog/', include('blog.urls')),
    path('user2/', include('user2.urls')),

    ]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

