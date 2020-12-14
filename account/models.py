from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User,related_name="user_ac",on_delete=models.CASCADE)
    is_servicer = models.BooleanField(default=False)
    address_fl = models.CharField(max_length=200,verbose_name="Address First Line")
    address_sl = models.CharField(max_length=200, verbose_name="Address Second Line")
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=6)
    mobile = models.CharField(max_length=12,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering= ["-created_at"]

