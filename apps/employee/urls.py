from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.employee.views import EmployeeViewSet

router = DefaultRouter()
router.register("", EmployeeViewSet)

urlpatterns = [path("", include(router.urls))]
