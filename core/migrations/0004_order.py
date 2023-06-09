# Generated by Django 3.2.7 on 2023-05-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gallery'),
    ]

    operations = [
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
    ]
