# Generated by Django 4.0 on 2023-02-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0008_remove_product_rating_delete_userrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rewiew', models.CharField(max_length=255, verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания отзыва')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления отзыва')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь')),
            ],
        ),
    ]
