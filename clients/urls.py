# clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Authentication
    path('signup/', views.client_signup, name='client_signup'),
    path('login/', views.client_login, name='client_login'),
    path('logout/', views.client_logout, name='client_logout'),

    # Dashboard & appointments
    path(
        'dashboard/',
        views.appointment_list,
        name='client_dashboard',
    ),
    path(
        'appointments/add/',
        views.appointment_create,
        name='client_create',
    ),
    path(
        'appointments/<int:pk>/edit/',
        views.appointment_update,
        name='client_update',
    ),

    # Clients profile edit & cancel capability
    path(
        'profile/edit/',
        views.client_edit_profile,
        name='client_profile',
    ),
    path(
        'appointments/<int:pk>/delete/',
        views.appointment_delete,
        name='client_delete_appointment',
    ),

    # Delete account
    path(
        'account/delete/',
        views.client_delete_account,
        name='account_delete',
    ),
]
