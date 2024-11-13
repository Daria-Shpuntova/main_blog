from django.contrib import admin
from .models import Course, Lesson, Komment, Articles, Direction, Otziv, Application

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Komment)
admin.site.register(Articles)
admin.site.register(Direction)
admin.site.register(Otziv)
admin.site.register(Application)