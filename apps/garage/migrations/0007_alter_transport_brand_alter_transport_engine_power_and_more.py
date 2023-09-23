# Generated by Django 4.2.5 on 2023-09-23 12:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0006_transport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='brand',
            field=models.CharField(max_length=30, null=True, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='engine_power',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='Мощность, л/с'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='engine_volume',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Объем двигателя, л'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='model',
            field=models.CharField(max_length=30, null=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='transport',
            name='odometer',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Пробег, км'),
        ),
    ]
