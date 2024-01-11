from rest_framework import serializers
from .models import Employee, Branch, Car

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Car
        fields = '__all__'
