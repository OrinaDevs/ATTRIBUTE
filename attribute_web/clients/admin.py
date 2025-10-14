from django.contrib import admin
from .models import Client, ClientService

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'status', 'start_date', 'end_date')
    list_filter = ('status',)
    search_fields = ('client_name', 'service_name')
