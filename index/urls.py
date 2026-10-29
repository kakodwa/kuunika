from django.urls import path
from .views import record_device_activity

urlpatterns = [
    path('api/track-activity/', record_device_activity, name='track_activity'),
]