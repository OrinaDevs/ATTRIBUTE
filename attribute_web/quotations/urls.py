from django.urls import path
from . import views

urlpatterns = [
    path('request/<int:service_id>/', views.request_quotation, name='request_quotation'),
    path('success/', views.quotation_success, name='quotation_success'),
]