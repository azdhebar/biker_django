from django.contrib import admin
from .models import  Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["pk","servicer","user","brand","model","solved"]
    list_filter = ["created_at","updated_at","solved"]
    search_fields = ["user","servicer"]

admin.site.register(Service,ServiceAdmin)

