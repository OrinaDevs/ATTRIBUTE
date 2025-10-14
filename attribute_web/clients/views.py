from django.shortcuts import render, get_object_or_404
from .models import Client, ClientService
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    services = ClientService.objects.filter(client=client)
    return render(request, 'client_detail.html', {
        'client': client,
        'services': services
    })