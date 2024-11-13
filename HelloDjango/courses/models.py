from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.


class Direction(models.Model):
    direction = models.CharField('Название направления', max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.direction


class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='course_img')
    free = models.BooleanField(default=True)
    direction = models.ManyToManyField(Direction)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_page', kwargs={'slug':self.slug})


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete= models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('les_page', kwargs={'slug':self.course.slug, 'les_slug':self.slug})


class Komment(models.Model):
    article = models.ForeignKey(Lesson, verbose_name='Слаг', on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
 #       print(self.Lesson)
        return f'Комментарий к лекции {self.article} автор {self.avtor}'

    class Meta:
        verbose_name = 'Комментарий',
        verbose_name_plural = 'Комментарии'


class Articles(models.Model):
    name = models.CharField('Название', max_length=150)
    data = models.DateField('Дата', default=timezone.now)
    text = models.TextField('Статья')
    direction = models.ManyToManyField(Direction)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name


class Otziv(models.Model):
    name = models.CharField('Имя', max_length=120)
    profession = models.CharField('Профессия', max_length=120)
    text = models.TextField('Текст комментария')
    img = models.ImageField(default='otziv.jpg', upload_to='otziv_img')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField('Имя', max_length=120)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                                 message="Номер телефона необходимо ввести в формате: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    email = models.CharField('E-mail', max_length=150)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name