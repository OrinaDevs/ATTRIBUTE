from django import forms
from .models import QuotationRequest

class QuotationRequestForm(forms.ModelForm):
    class Meta:
        model = QuotationRequest
        fields = ['service', 'client_name', 'client_email', 'client_phone', 'additional_details']