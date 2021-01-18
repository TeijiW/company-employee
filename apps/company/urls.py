from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.company.views import CompanyViewSet

router = DefaultRouter()
router.register("", CompanyViewSet)

urlpatterns = [path("", include(router.urls))]