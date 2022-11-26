from django.contrib.auth import get_user_model
from django.db import models


class Picture(models.Model):
    description = models.CharField(verbose_name='Подпись', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=False, upload_to='pictures')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
