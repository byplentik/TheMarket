# Generated by Django 4.0 on 2023-02-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_rewiew_review_review_review_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=255, null=True, verbose_name='Отзыв'),
        ),
    ]