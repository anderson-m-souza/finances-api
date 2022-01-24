from django.db import models
from django.utils import timezone


class Income(models.Model):
    description = models.CharField(
        db_column='description',
        verbose_name='Description',
        max_length=255,
        blank=False,
        null=False)
    value = models.DecimalField(
        db_column='value',
        verbose_name='Value',
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False)
    date = models.DateField(
        db_column='date',
        verbose_name='Date',
        default=timezone.now,
        blank=False,
        null=False)

    def __str__(self):
        return f"description: {self.description}, value: {self.value}, date: {self.date}"

    class Meta:
        db_table = 'income'
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'


class Expense(models.Model):
    description = models.CharField(
        db_column='description',
        verbose_name='Description',
        max_length=255,
        blank=False,
        null=False)
    value = models.DecimalField(
        db_column='value',
        verbose_name='Value',
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=False)
    date = models.DateField(
        db_column='date',
        verbose_name='Date',
        default=timezone.now,
        blank=False,
        null=False)

    def __str__(self):
        return f"description: {self.description}, value: {self.value}, date: {self.date}"

    class Meta:
        db_table = 'expense'
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'