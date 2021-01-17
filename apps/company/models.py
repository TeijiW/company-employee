from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employees = models.ManyToManyField(
        "employee.Employee", related_name="companies", blank=True
    )

    def __str__(self):
        return self.name