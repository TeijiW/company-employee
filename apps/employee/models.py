from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    name = models.CharField(max_length=256)
    username = models.CharField(
        max_length=256,
        unique=True,
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name