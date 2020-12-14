from zipfile import Path

from django.contrib import admin
from .models import Account

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ["user","is_servicer"]
    list_filter = ["created_at","updated_at","is_servicer"]
    search_fields = ["user"]

admin.site.register(Account,AccountAdmin)
