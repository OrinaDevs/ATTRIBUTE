from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# ===============================
# REGISTER (CUSTOM)
# ===============================
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'account/signup.html', {'form': form})
