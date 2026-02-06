from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuotationRequestForm
from services.models import Service


@login_required
def request_quotation(request, service_id=None):
    if request.method == 'POST':
        form = QuotationRequestForm(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)


            # Auto-fill user details
            quotation.user = request.user
            quotation.client_name = request.user.get_full_name() or request.user.username
            quotation.client_email = request.user.email


            quotation.save()
            return redirect('my_quotations')
    else:
        form = QuotationRequestForm(initial={
            'service': service_id,
            'client_name': request.user.get_full_name() or request.user.username,
            'client_name': request.user.email,
        })

    return render(request, 'request_quotation.html', {'form': form})

def quotation_success(request):
    return render(request, 'quotation_success.html')

@login_required
def my_quotations(request):
    quotations = request.user.quotations.select_related('service').order_by('-created_at')
    return render(request, 'my_quotations.html', {'quotations': quotations})