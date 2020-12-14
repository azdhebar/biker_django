from django.db import models
from brand.models import Brand
# Create your models here.
class Models(models.Model):
    model_name = models.CharField(max_length=100,verbose_name="Model Name")
    status = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand,related_name="model_brand",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Models"
        verbose_name = "Model"
