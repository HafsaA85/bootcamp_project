from django.shortcuts import render, redirect
from .forms import ClientSignupForm, ClientLoginForm
from .models import Client


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

# Create
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Add Client'})

# Read (List all clients)
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

# Update
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form, 'title': 'Edit Client'})

# Delete
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})