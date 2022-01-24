from rest_framework import serializers
from finances.models import Income, Expense


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

    def update(self, instance, attrs):
        same_description_and_month = Income.objects.filter(
            description=attrs['description'],
            date__month=attrs['date'].month,
            date__year=attrs['date'].year
        ).exclude(id=instance.id)
        
        if same_description_and_month.exists():
            raise serializers.ValidationError('There is already an item with this description in this month.')
        
        instance.description=attrs['description']
        instance.value=attrs['value']
        instance.date=attrs['date']
        instance.save()

        return instance


    def create(self, attrs):
        same_description_and_month = Income.objects.filter(
            description=attrs['description'],
            date__month=attrs['date'].month,
            date__year=attrs['date'].year
        )

        if same_description_and_month.exists():
            raise serializers.ValidationError('There is already an item with this description in this month.')

        return Income.objects.create(**attrs)


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def update(self, instance, attrs):
        same_description_and_month = Expense.objects.filter(
            description=attrs['description'],
            date__month=attrs['date'].month,
            date__year=attrs['date'].year
        ).exclude(id=instance.id)
        
        if same_description_and_month.exists():
            raise serializers.ValidationError('There is already an item with this description in this month.')
        
        instance.description=attrs['description']
        instance.value=attrs['value']
        instance.date=attrs['date']
        instance.save()

        return instance


    def create(self, attrs):
        same_description_and_month = Expense.objects.filter(
            description=attrs['description'],
            date__month=attrs['date'].month,
            date__year=attrs['date'].year
        )
        
        if same_description_and_month.exists():
            raise serializers.ValidationError('There is already an item with this description in this month.')
        print('create')
        return Expense.objects.create(**attrs)
