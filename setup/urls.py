from django.contrib import admin
from django.urls import path, include
from finances.views import IncomesViewset, ExpenseViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('incomes', IncomesViewset, basename='Incomes')
router.register('expenses', ExpenseViewset, basename='Expenses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
