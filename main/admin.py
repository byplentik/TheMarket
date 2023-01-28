from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ImageForProduct)
class ImageForProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'img_product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    prepopulated_fields = {'slug': ('name',)}

    

