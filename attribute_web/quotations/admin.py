from django.contrib import admin
from .models import QuotationRequest
from clients.models import Client, ClientService

# Register your models here.
@admin.register(QuotationRequest)
class QuotationRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'client_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('client_name', 'client_email', 'service_name')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        # When status changes to approved → create ClientService
        if obj.status == 'approved':
            # Try to find or create client
            client, created = Client.objects.get_or_create(
                email=obj.client_email,
                defaults={
                    'name': obj.client_name,
                    'phone': obj.client_phone,
                }
            )
            obj.client = client
            obj.save()

            # Create ClientService if not already existing
            ClientService.objects.get_or_create(
                client=client,
                service=obj.service,
                defaults={'status': 'not_started'}
            )