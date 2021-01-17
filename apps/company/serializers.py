from rest_framework import serializers
from apps.company.models import Company
from apps.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "email",
            "name",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "id",
            "is_active",
        ]


class CompanySerializer(serializers.ModelSerializer):

    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
            "city",
            "country",
            "employees",
        ]
        read_only_fields = ["created_at", "updated_at", "id", "employees"]
        # fields = []
        # read_only_fields = []

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    # def __init__(self, *args, **kwargs):
    #     context = kwargs.get("context", {})
    #     get_employees = context.get("get_employees")

    #     self.Meta.fields = [
    #         "id",
    #         "name",
    #         "created_at",
    #         "updated_at",
    #         "city",
    #         "country",
    #         "employees",
    #     ]
    #     self.Meta.read_only_fields = ["created_at", "updated_at", "id", "employees"]
    #     if not get_employees:
    #         self.Meta.fields.remove("employees")

    #     super(CompanySerializer, self).__init__(*args, **kwargs)

    def get_employees(self, obj):
        employees = obj.employees.all()
        return EmployeeSerializer(instance=employees, many=True, read_only=True).data
