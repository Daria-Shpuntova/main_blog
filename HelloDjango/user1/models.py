from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

TYPE_CHOS = (
    ('Полный пакет', 'full'),
    ('Бесплатный пакет', 'free')
)

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='7065729.png', upload_to='user_img')
    ac_type = models.CharField(choices=TYPE_CHOS, default='Бесплатный пакет', max_length=30)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width >256:
            resize = (256,256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл',
        verbose_name_plural = 'Профайлы'
