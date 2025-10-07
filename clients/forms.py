# clients/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Client, Appointment


# Signup form using email as username

class ClientSignupForm(forms.Form):
    full_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))


# Method to validate phone
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
#validation for phone to be digits only        
        if phone and not phone.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")
        return phone
    

# clients/profile 

class ClientProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['phone']  # phone is on Client model

    def __init__(self, *args, **kwargs):
        # Pass instance of User if editing
        user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        if user_instance:
            self.fields['full_name'].initial = user_instance.first_name
            self.fields['email'].initial = user_instance.email

    def save(self, commit=True):
        client = super().save(commit=False)
        user = client.user
        user.first_name = self.cleaned_data['full_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            client.save()
        return client


class ClientLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['title', 'date', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
