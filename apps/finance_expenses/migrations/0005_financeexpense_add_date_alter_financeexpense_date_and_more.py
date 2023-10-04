# Generated by Django 4.2.5 on 2023-09-28 16:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance_expenses', '0004_financeexpense'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeexpense',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='financeexpense',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Выберите дату', validators=[django.core.validators.MaxValueValidator(django.utils.timezone.now)], verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='financeexpense',
            name='expense_type',
            field=models.ForeignKey(help_text='Выберите категорию расходов', null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance_expenses.expensetypes'),
        ),
        migrations.AlterField(
            model_name='financeexpense',
            name='odometer',
            field=models.IntegerField(default=1, help_text='Укажите пробег, на момент траты средств', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Пробег'),
        ),
        migrations.AlterField(
            model_name='financeexpense',
            name='summ',
            field=models.FloatField(default=1, help_text='Укажите сумму израсходованных средств.', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Сумма'),
        ),
    ]