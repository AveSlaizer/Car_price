# Generated by Django 4.2.5 on 2023-10-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/main_page/carousel/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Карусель главной страницы',
                'verbose_name_plural': 'Карусель главной страницы',
            },
        ),
    ]
