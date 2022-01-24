# Generated by Django 4.0.1 on 2022-01-20 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=255, verbose_name='Description')),
                ('value', models.DecimalField(db_column='value', decimal_places=2, max_digits=7, verbose_name='Value')),
                ('date', models.DateField(db_column='date', default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
                'db_table': 'expense',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=255, verbose_name='Description')),
                ('value', models.DecimalField(db_column='value', decimal_places=2, max_digits=7, verbose_name='Value')),
                ('date', models.DateField(db_column='date', default=django.utils.timezone.now, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Incomes',
                'db_table': 'income',
            },
        ),
    ]
