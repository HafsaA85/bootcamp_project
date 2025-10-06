# clients/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ClientSignupForm, ClientLoginForm, AppointmentForm
from .models import Client, Appointment

# -------------------
# Homepage
# -------------------
def home(request):
    return render(request, 'clients/home.html')

# -------------------
# Signup
# -------------------
def client_signup(request):
    if request.method == 'POST':
        form = ClientSignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']

            # Create User
            user = User.objects.create_user(username=email, email=email, password=password, first_name=full_name)
            
            # Create Client profile
            client = Client.objects.create(user=user, phone=phone)

            login(request, user)
            messages.success(request, "Signup successful! Welcome.")
            return redirect('client_dashboard')
    else:
        form = ClientSignupForm()
    return render(request, 'clients/client_signup.html', {'form': form})

# -------------------
# Login / Logout
# -------------------
# clients/views.py (login view)

def client_login(request):
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # email is used as username
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('client_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = ClientLoginForm()
    return render(request, 'clients/client_login.html', {'form': form})


def client_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

# -------------------
# Appointments (CRUD)
# -------------------
@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(client__user=request.user)
    return render(request, 'clients/client_dashboard.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = get_object_or_404(Client, user=request.user)
            appointment.save()
            messages.success(request, "Appointment created successfully!")
            return redirect('client_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'clients/appointment_form.html', {'form': form, 'title': 'Book New Appointment'})

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, client__user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment updated successfully!")
            return redirect('client_dashboard')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'clients/appointment_form.html', {'form': form, 'title': 'Edit Appointment'})

# -------------------
# Delete own account
# -------------------
@login_required
def client_delete_account(request):
    client = get_object_or_404(Client, user=request.user)
    if request.method == 'POST':
        user = client.user
        client.delete()
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})
