# Generated by Django 4.2.5 on 2023-10-04 15:51

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_expenses', '0009_alter_financeexpense_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensetypes',
            options={'verbose_name': 'Категория трат на ТС', 'verbose_name_plural': 'Категории трат на ТС'},
        ),
        migrations.AlterModelOptions(
            name='financeexpense',
            options={'ordering': ['add_date'], 'verbose_name': 'Трата на ТС', 'verbose_name_plural': 'Траты на ТС'},
        ),
        migrations.AlterField(
            model_name='financeexpense',
            name='date',
            field=models.DateField(default=datetime.date(2023, 10, 4), help_text='Выберите дату', validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 10, 4))], verbose_name='Дата трат'),
        ),
    ]