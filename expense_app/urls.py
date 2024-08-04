from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListExpenseView.as_view(), name="get-all-expense"),
    path("create/", views.CreateExpense.as_view(), name="create-expense"),
    path(
        "update/<int:pk>/",
        views.RetrieveUpdateExpense.as_view(),
        name="retrieve-update",
    ),
    path(
        "delete/<int:pk>/",
        views.DeleteExpenseView.as_view(),
        name="delete-expense",
    ),
]
