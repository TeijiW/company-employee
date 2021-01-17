from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.company.models import Company
from apps.company.serializers import CompanySerializer
from apps.employee.models import Employee


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    @action(
        methods=["PUT", "DELETE"],
        detail=True,
        url_path=r"employee/(?P<employee_id>\d+)",
    )
    def employee_relation(self, request, pk, employee_id):
        try:
            company = Company.objects.get(pk=pk)
            employee = Employee.objects.get(pk=employee_id)
            if request.method == "PUT":
                company.employees.add(employee)
            elif request.method == "DELETE":
                company.employees.remove(employee)
            company.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except company.DoesNotExist or company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)