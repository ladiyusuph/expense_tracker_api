from django.db import models
from django.contrib.auth.models import User


class ExpenseTable(models.Model):
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.ManyToManyField(
        "Category", related_name="expense_category", blank=True
    )
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
