from django.shortcuts import render, redirect
from .forms import QuotationRequestForm

# Create your views here.
def request_quotation(request, service_id=None):
    if request.method =='POST':
        form = QuotationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotation_success')
    
    else:
        if service_id:
            form = QuotationRequestForm(initial={'service': service_id})
        
        else:
            form = QuotationRequestForm()
    return render(request, 'request_quotation.html', {'form': form})

def quotation_success(request):
    return render(request, 'quotation_success.html')