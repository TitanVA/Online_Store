# Generated by Django 3.2.9 on 2021-12-13 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_review_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='parent',
        ),
    ]
