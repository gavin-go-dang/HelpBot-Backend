from django.contrib import admin

from .models import Project, Room


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at")
    fieldsets = [
        (None, {"fields": [("name"), ("owner")]}),
    ]
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "id_synapse", "created_at")
    fieldsets = [
        (None, {"fields": [("project")]}),
    ]
    search_fields = ("name",)
