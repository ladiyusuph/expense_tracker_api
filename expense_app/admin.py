from django.contrib import admin
from .models import ExpenseTable, Category

admin.site.register(Category)
admin.site.register(ExpenseTable)
