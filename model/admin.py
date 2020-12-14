from django.contrib import admin
from .models import Models
# Register your models here.
class ModelsAdmin(admin.ModelAdmin):
    list_display = ["model_name","brand","status"]
    list_filter = ["created_at","updated_at","brand","status"]
    search_fields = ["model_name"]


admin.site.register(Models,ModelsAdmin)