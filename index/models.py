from django.db import models

class AppInstall(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    installed_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    open_count = models.PositiveIntegerField(default=1)
    app_version = models.CharField(max_length=20, default="1.0.0")

    def __str__(self):
        return f"{self.device_id} (Opened: {self.open_count} times)"