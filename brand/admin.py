from django.contrib import admin
from .models import  Brand
from model.models import Models
# Register your models here.
class ModelInline(admin.TabularInline):
    model = Models

class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand","logo","status"]
    list_filter = ["created_at","updated_at","status"]
    search_fields = ["brand"],
    inlines = [ModelInline]

admin.site.register(Brand,BrandAdmin)