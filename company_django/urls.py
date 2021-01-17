from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/company/", include("apps.company.urls")),
    path("api/employee/", include("apps.employee.urls")),
    path("api/api-token-auth/", obtain_auth_token),
]