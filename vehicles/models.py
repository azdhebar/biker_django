from django.db import models
from account.models import Account
from model.models import Models
# Create your models here.

class Vehicle(models.Model):
    vehicle_number=models.CharField(max_length=20)
    model_fk = models.ForeignKey(Models,related_name="model_vehicle",on_delete=models.CASCADE)
    user = models.ForeignKey(Account,related_name="account_vehicle",on_delete=models.CASCADE)
    status= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_number

    class Meta:
        ordering = ["-created_at"]
    
    