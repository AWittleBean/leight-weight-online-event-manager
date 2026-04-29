from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
        "host",
    )


admin.site.register(Event, EventAdmin)
