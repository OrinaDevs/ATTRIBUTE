from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # IMPORTANT: specify backend manually
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user) #Auto Login after Registration
            return redirect('index') #Redirects to home page
    else:
        form = CustomUserCreationForm(request.POST)
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')


