# clients/models.py
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="appointments")
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.client.user.username}"


class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.client.user.username}: {self.message}"
