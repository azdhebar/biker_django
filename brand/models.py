from django.db import models

# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=100)
    logo = models.ImageField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

    class Meta:
        ordering= ["-created_at"]
