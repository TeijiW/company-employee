import json
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from apps.employee.models import Employee


class EmployeeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="John Doe", password="123")
        self.client.force_authenticate(user=self.user)
        self.default_company_obj = {
            "name": "Test",
            "country": "Brazil",
            "city": "Rio de Janeiro",
        }
        self.default_employee_obj = {
            "name": "John Doe",
            "username": "john_doe",
            "email": "john_doe@test.com",
        }

    def test_get_single_employee(self):
        response = self.client.post(
            "/api/employee/",
            self.default_employee_obj,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/employee/{}/".format(response.data.get("id")))
        self.assertEqual(response.status_code, 200)

    def test_get_not_existent_employee(self):
        response = self.client.get("/api/employee/{}/".format(311))
        self.assertEqual(response.status_code, 404)

    def test_create(self):
        response = self.client.post(
            "/api/employee/",
            self.default_employee_obj,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

    def test_create_without_required_fields(self):
        response = self.client.post(
            "/api/employee/",
            {"country": "Brazil", "city": "Rio de Janeiro"},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_update(self):
        response = self.client.post(
            "/api/employee/",
            self.default_employee_obj,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        updated_object = {
            "name": "Doe John",
            "email": "tests@tests.com",
            "username": "doe_john",
        }
        response = self.client.put(
            "/api/employee/{}/".format(response.data.get("id")),
            updated_object,
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], updated_object["name"])
        self.assertEqual(response.data["email"], updated_object["email"])

    def test_delete(self):
        response = self.client.post(
            "/api/employee/",
            self.default_employee_obj,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.delete(
            "/api/employee/{}/".format(response.data.get("id"))
        )
        self.assertEqual(response.status_code, 204)

    def test_insert_company(self):
        employee_response = self.client.post(
            "/api/employee/",
            self.default_employee_obj,
            format="json",
        )
        self.assertEqual(employee_response.status_code, 201)
        employee_id = employee_response.data.get("id")

        company_response = self.client.post(
            "/api/company/",
            self.default_company_obj,
            format="json",
        )
        self.assertEqual(company_response.status_code, 201)
        company_id = company_response.data.get("id")

        response = self.client.put(
            "/api/employee/{}/company/{}/".format(employee_id, company_id),
            format="json",
        )
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/api/employee/{}/".format(employee_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data.get("companies")), 1)
