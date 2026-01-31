from zoneinfo import ZoneInfo

from apps.payment.models import Payment
from django.contrib import admin

TEHRAN_TZ = ZoneInfo("Asia/Tehran")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "amount", "created_at_tehran", "status")
    search_fields = ("order_id", "full_name", "authority")
    list_filter = ("status",)
    ordering = ("-id", )

    def created_at_tehran(self, obj):
        if not obj.created_at:
            return "-"
        tehran_time = obj.created_at.astimezone(TEHRAN_TZ)
        return tehran_time.strftime("%Y-%m-%d %H:%M:%S")

    created_at_tehran.short_description = "Created At (Tehran)"
