# Generated by Django 4.0 on 2023-03-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(5, 'Отлично'), (4, 'Хорошо'), (3, 'Нормально'), (2, 'Плохо'), (1, 'Ужасно')], verbose_name='Оценка'),
        ),
    ]