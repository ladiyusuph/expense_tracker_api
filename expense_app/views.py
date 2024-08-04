from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ExpenseSerializer
from .models import ExpenseTable, Category
from datetime import datetime, timedelta
from django.utils.timezone import now


class ListExpenseView(GenericAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        period = self.request.query_params.get("period")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        # Get today's date
        today = now().date()

        # Calculate date ranges based on the period
        if period == "past_week":
            start = today - timedelta(days=7)
            end = today
        elif period == "last_3_months":
            start = today - timedelta(days=90)
            end = today
        elif period == "last_month":
            start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
            end = start.replace(day=1) - timedelta(days=1)
        elif period == "custom" and start_date and end_date:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
        else:
            return ExpenseTable.objects.filter(owner=user)

        # Return filtered queryset based on date range and owner
        return ExpenseTable.objects.filter(owner=user, date__range=(start, end))

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        expense_data = []
        for expense in serializer.data:
            expense = {
                "name": expense.get("name", "string"),
                "description": expense.get("description", "string"),
            }
            expense_data.append(expense)

        response_data = {
            "status": "success",
            "data": {"expenses": expense_data},
        }
        return Response(response_data, status=status.HTTP_200_OK)


class CreateExpense(CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateExpense(RetrieveUpdateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseTable.objects.filter(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            category_name = validated_data.pop("category", None)
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            instance.category.clear()
            instance.category.add(category)

        return Response(serializer.data)


class DeleteExpenseView(DestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseTable.objects.filter(owner=self.request.user)
