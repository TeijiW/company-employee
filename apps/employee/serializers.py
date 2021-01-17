from rest_framework import serializers
from apps.employee.models import Employee
from apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
        ]

        read_only_fields = ["id", "name"]


class EmployeeSerializer(serializers.ModelSerializer):

    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "email",
            "name",
            "created_at",
            "updated_at",
            "companies",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "id",
            "companies",
        ]

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
