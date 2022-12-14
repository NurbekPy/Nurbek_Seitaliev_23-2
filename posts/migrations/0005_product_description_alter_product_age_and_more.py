# Generated by Django 4.1.4 on 2022-12-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_product_author_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
