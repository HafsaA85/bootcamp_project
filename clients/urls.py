# clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.client_signup, name='client_signup'),
    path('signup-success/', views.signup_success, name='signup_success'),
    path('login/', views.client_login, name='client_login'),  # if you have login view
]
