# Generated by Django 4.0 on 2023-02-04 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.DeleteModel(
            name='UserRating',
        ),
    ]
