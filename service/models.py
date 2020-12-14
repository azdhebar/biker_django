from django.db import models
from account.models import Account
from brand.models import Brand
from model.models import Models
from vehicles.models import Vehicle

# Create your models here.
class Service(models.Model):
    servicer = models.ForeignKey(Account,related_name="servicer_service",on_delete=models.CASCADE)
    user = models.ForeignKey(Account,related_name="user_service",on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="brand_service", on_delete=models.CASCADE)
    vehicle_fk = models.ForeignKey(Vehicle,related_name="vehicle_service",on_delete=models.CASCADE,default=None)
    model_fk = models.ForeignKey(Models, related_name="model_service", on_delete=models.CASCADE)
    problem = models.TextField()
    problem_image = models.ImageField(verbose_name="Problem Image")
    solved = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    remarks = models.TextField(default="",blank=True)
    review = models.TextField(default="",blank=True)
    cancel_user = models.BooleanField(default=False)
    cancel_servicer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        ordering = ["-created_at"]


