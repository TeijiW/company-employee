from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.company.models import Company
from apps.employee.models import Employee
from apps.employee.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    @action(
        url_path=r"username/(?P<employee_username>\w+)",
        detail=False,
        name="Get by username",
    )
    def get_by_username(self, request, employee_username):
        try:
            employee = Employee.objects.get(username=employee_username)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(
        methods=["PUT", "DELETE"], detail=True, url_path=r"company/(?P<company_id>\d+)"
    )
    def company_relation(self, request, pk, company_id):
        try:
            employee = Employee.objects.get(pk=pk)
            company = Company.objects.get(pk=company_id)
            if request.method == "PUT":
                employee.companies.add(company)
            elif request.method == "DELETE":
                employee.companies.remove(company)
            employee.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except employee.DoesNotExist or company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)