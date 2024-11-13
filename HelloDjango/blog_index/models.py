from django.db import models
from django.urls import reverse
# Create your models here.

class Progects(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название проекта')
    text = models.TextField(verbose_name='Описание проекта')
    img = models.ImageField(verbose_name='Скрин', default=None, upload_to='skrins')
    link_github = models.CharField(max_length=300, verbose_name='Ссылка на GitHub')
    link_progect=models.CharField(max_length=250, verbose_name='Ссылка на проект')
    link_figma = models.CharField(max_length=250, blank=True, verbose_name='Ссылка на Figma')
    tags = models.ManyToManyField('Tags', blank=True, related_name='tags', verbose_name="Тэги")
    data = models.DateField(blank=True,verbose_name='Дата')
#    tag = models.ManyToManyField()

    def __str__(self):
        return f'Проект {self.title}'

    def get_absolute_url(self):
        return reverse('prog_id', kwargs={'prog_id':self.id })

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-data']


class Tags(models.Model):
    tag=models.CharField(max_length=100, verbose_name='Тег')
    svg = models.TextField(verbose_name='svg код', blank=True)
    text_tag = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.tag
