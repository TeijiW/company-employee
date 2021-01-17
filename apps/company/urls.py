from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.company.views import CompanyViewSet

router = DefaultRouter()
router.register("", CompanyViewSet)

urlpatterns = [path("", include(router.urls))]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from apps.company.views import (
#     CompanyListOrCreate,
#     CompanyDetailUpdateDelete,
#     insert_employee,
#     remove_employee,
#     get_company_employees,
# )


# urlpatterns = [
#     path("", CompanyListOrCreate.as_view()),
#     path("<int:pk>/", CompanyDetailUpdateDelete.as_view()),
#     path("<int:pk>/employee/<int:employee_id>", insert_employee),
#     path("<int:pk>/employee/<int:employee_id>", remove_employee),
#     path("<int:pk>/employee", get_company_employees),
# ]
