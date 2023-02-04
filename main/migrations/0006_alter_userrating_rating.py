# Generated by Django 4.0 on 2023-02-03 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='рейтинг'),
        ),
    ]