from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

#custom Django management command in your project that creates a superuser programmatically
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword')
            self.stdout.write('Superuser created')
        else:
            self.stdout.write('Superuser already exists')