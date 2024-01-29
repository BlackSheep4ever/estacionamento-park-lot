from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Card_id = models.CharField(max_length=10, blank=True, null=True)

class Vehicle(models.Model):
    Id = models.AutoField(primary_key=True)
    Plate = models.CharField(max_length=10)
    Model = models.CharField(max_length=30, blank=True, null=True)
    Description = models.CharField(max_length=50, blank=True, null=True)
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

class Plan(models.Model):
    Id = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=50)
    Value = models.FloatField()

class Customer_Plan(models.Model):
    Id = models.AutoField(primary_key=True)
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Due_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

class Contract(models.Model):
    Id = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=50)
    Max_value = models.FloatField(blank=True, null=True)

class Contract_Rule(models.Model):
    Id = models.AutoField(primary_key=True)
    Contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    Until = models.IntegerField()
    Value = models.FloatField()

class Parkmovement(models.Model):
    Id = models.AutoField(primary_key=True)
    Entry_date = models.DateTimeField(default=timezone.now)
    Exit_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Value = models.FloatField(blank=True, null=True)