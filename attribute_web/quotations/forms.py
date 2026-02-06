from django import forms
from .models import QuotationRequest


class QuotationRequestForm(forms.ModelForm):
    class Meta:
        model = QuotationRequest
        fields = [
            'service',
            'client_name',
            'client_email',
            'client_phone',
            'additional_details',
        ]

        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-select',
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name',
            }),
            'client_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address',
            }),
            'client_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number',
            }),
            'additional_details': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Provide additional details about the service you need...',
            }),
        }
