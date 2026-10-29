from django.contrib import admin
from .models import AppInstall

@admin.register(AppInstall)
class AppInstallAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'installed_at', 'last_active', 'open_count', 'app_version')
    search_fields = ('device_id',)