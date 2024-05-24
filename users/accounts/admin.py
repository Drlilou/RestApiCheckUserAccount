from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'firstname', 'lastname','date_joined', 'is_active')
    search_fields = ('email', 'username', 'firstname')
    list_filter = ('is_active', 'date_joined')
    ordering = ('-date_joined',)
