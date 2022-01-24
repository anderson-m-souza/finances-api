from rest_framework import viewsets
from finances.models import Income, Expense
from finances.serializer import IncomeSerializer, ExpenseSerializer


class IncomesViewset(viewsets.ModelViewSet):
    """Show all incomes"""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenseViewset(viewsets.ModelViewSet):
    """Show all expenses"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
