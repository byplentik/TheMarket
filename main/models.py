from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class ImageForProduct(models.Model):
    img_product = models.ImageField(upload_to='products/')
    

    class Meta:
        verbose_name = ("ImageForProducts")
        verbose_name_plural = ("ImageForProducts")


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Модель')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Рейтинг')
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
