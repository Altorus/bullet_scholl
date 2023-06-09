# Generated by Django 3.2.7 on 2023-06-01 16:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_auto_20230601_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='gallery', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(max_length=200, verbose_name='Урл страницы')),
                ('seo_h1', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO H1')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='SEO description')),
                ('seo_keywords', models.CharField(blank=True, max_length=500, null=True, verbose_name='SEO keywords')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контент')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('photo', models.FileField(upload_to='news', verbose_name='Фото')),
                ('dt_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('dt_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.SlugField(max_length=200, verbose_name='Урл страницы')),
                ('seo_h1', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO H1')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='SEO description')),
                ('seo_keywords', models.CharField(blank=True, max_length=500, null=True, verbose_name='SEO keywords')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контент')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('menushow', models.BooleanField(default=False, verbose_name='Показывать в меню')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
