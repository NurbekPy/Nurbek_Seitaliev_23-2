# Generated by Django 4.1.4 on 2022-12-15 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
