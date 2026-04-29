from django.contrib import admin

# Register your models here.
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "host",
        "date",
        "member_list_display",
    )

    def member_list_display(self, obj):
        return ", ".join([m.username for m in obj.member_list.all()])

    member_list_display.short_description = "Members"


admin.site.register(Event, EventAdmin)
