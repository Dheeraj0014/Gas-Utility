from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  address = models.TextField()
  phone_number = models.CharField(max_length=20)


class ServiceRequest(models.Model):
  SERVICE_TYPE_CHOICES = (
      ('NEW_CONNECTION', 'New Connection'),
      ('METER_REPAIR', 'Meter Repair'),
      ('LEAK_DETECTION', 'Leak Detection'),
  )
  type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
  description = models.TextField()
  urgency_level = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'),
                                               (3, 'High')))
  status = models.CharField(max_length=20, default='PENDING')
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  assigned_to = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)


class Account(models.Model):
  customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
  account_number = models.CharField(max_length=20)
