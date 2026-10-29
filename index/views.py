import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import AppInstall

@csrf_exempt
def record_device_activity(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            device_id = data.get("device_id")
            session_count = data.get("session_count", 1)
            app_version = data.get("app_version", "1.0.0")

            if not device_id:
                return JsonResponse({"error": "device_id is required"}, status=400)

            install_record, created = AppInstall.objects.get_or_create(
                device_id=device_id,
                defaults={
                    "open_count": session_count,
                    "app_version": app_version,
                }
            )

            if not created:
                # Add any offline sessions recorded by the device
                install_record.open_count += session_count
                install_record.app_version = app_version
                install_record.last_active = timezone.now()
                install_record.save()

            return JsonResponse({
                "status": "success",
                "is_first_install": created,
                "total_opens": install_record.open_count
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST method required"}, status=405)