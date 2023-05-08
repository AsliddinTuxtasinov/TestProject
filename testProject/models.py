from django.db import models
from simple_history.models import HistoricalRecords


class TestModel(models.Model):
    test_name = models.CharField(max_length=255)

    def __str__(self):
        return self.test_name


class EmailSubscribed(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Permission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)
    partition = models.ManyToManyField(Permission)
    created_date = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name
