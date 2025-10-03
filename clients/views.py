from django.shortcuts import render, redirect
from .forms import ClientSignupForm, ClientLoginForm


def home(request):
    return render(request, 'clients/home.html')


def client_signup(request):
    if request.method == 'POST':
        form = ClientSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a separate success page
            return redirect('signup_success')
    else:
        form = ClientSignupForm()
    return render(request, 'clients/client_signup.html', {'form': form})


def signup_success(request):
    # Simple success page
    return render(request, 'clients/signup_success.html')

def client_login(request):
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Add authentication logic here
    else:
        form = ClientLoginForm()
    return render(request, 'clients/login.html', {'form': form})

