from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class News(models.Model):
    title = models.CharField('Название статьи',max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата',default=timezone.now)
    avt = models.ForeignKey(User,verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры',default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return f'Новость : {self.title}'

    class Meta:
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'


class Komment2(models.Model):
    article = models.ForeignKey(News, verbose_name='Cтатья', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default=timezone.now)
    avt = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'Комментарий к статье {self.article} автор {self.avt}'

    class Meta:
        verbose_name = 'Комментарий',
        verbose_name_plural = 'Комментарии'