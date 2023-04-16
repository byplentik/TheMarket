from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, verbose_name='Фото профиля', default='images.png')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"slug": self.slug})
    
