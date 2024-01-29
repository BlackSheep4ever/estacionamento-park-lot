from rest_framework import serializers
from CloudPark.models import Customer, Vehicle, Plan, Contract, Customer_Plan, Contract_Rule, Parkmovement

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('Id', 'Name', 'Card_id')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('Id', 'Plate', 'Model', 'Description', 'Customer_id')

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('Id', 'Description', 'Value')

class Customer_PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Plan
        fields = ('Id', 'Customer_id', 'Plan_id', 'Due_date')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('Id', 'Description', 'Max_value')

class Contract_RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract_Rule
        fields = ('Id', 'Contract_id', 'Until', 'Value')

class ParkmovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkmovement
        fields = ('Id', 'Entry_date', 'Exit_date', 'Vehicle_id', 'Value')