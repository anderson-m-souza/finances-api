from django.contrib import admin
from finances.models import Income, Expense


class Incomes(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'date')
    list_display_links = ('id', 'description')
    search_fields = ('description',)
    list_per_page = 10

admin.site.register(Income, Incomes)

class Expenses(admin.ModelAdmin):
    list_display = ('id', 'description', 'value', 'date')
    list_display_links = ('id', 'description')
    search_fields = ('description',)
    list_per_page = 10

admin.site.register(Expense, Expenses)