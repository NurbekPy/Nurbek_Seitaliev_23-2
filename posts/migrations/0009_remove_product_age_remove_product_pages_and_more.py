# Generated by Django 4.1.4 on 2023-01-01 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_hashtag_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='age',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='product',
            name='publish_year',
        ),
    ]
