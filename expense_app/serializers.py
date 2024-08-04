from rest_framework import serializers
from .models import Category, ExpenseTable


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ExpenseTable
        fields = ["date", "name", "description", "amount", "category", "owner"]

    def create(self, validated_data):
        categories_data = validated_data.pop("category")
        expense = ExpenseTable.objects.create(**validated_data)
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            expense.category.add(category)
        expense.save()
        return expense

    # def update(self, instance, validated_data):
    #     category_name = validated_data.pop("category", None)
    #     if category_name:
    #         category, created = Category.objects.get_or_create(name=category_name)
    #         instance.category.clear()
    #         instance.category.add(category)
    #     return super().update(instance, validated_data)
