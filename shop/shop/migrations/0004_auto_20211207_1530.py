# Generated by Django 3.2.9 on 2021-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211207_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reviews',
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Review', verbose_name='Отзывы'),
        ),
    ]
