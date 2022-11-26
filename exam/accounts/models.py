from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, blank=True)
    favorite_pictures = models.ManyToManyField(verbose_name='Избранные фотографии', to='gallery.Picture',
                                               related_name='user_favorite')

    # commented_posts = models.ManyToManyField(verbose_name='Прокомментированные публикации', to='posts.Post',
    #                                          related_name='user_comments')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.email} {self.username}'
