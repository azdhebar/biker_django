from django.db import models
from account.models import Account
from brand.models import Brand
from model.models import Models

# Create your models here.
class Servicer(models.Model):
    user = models.ForeignKey(Account,related_name="account_servicer",on_delete=models.CASCADE)
    model_fk = models.ForeignKey(Models,related_name="model_servicer",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model_fk.model_name

    class Meta:
        ordering = ["-created_at"]

