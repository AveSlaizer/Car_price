# Generated by Django 4.2.5 on 2023-09-22 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance_expenses', '0002_alter_financeexpense_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FinanceExpense',
        ),
    ]