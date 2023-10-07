from django.contrib import admin

from .models import Project, Room, Question, Answer


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at")
    fieldsets = [
        (None, {"fields": [("name"), ("owner"), ("script_QA")]}),
    ]
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "id_synapse", "created_at")
    fieldsets = [
        (None, {"fields": [("project"), ("id_synapse")]}),
    ]
    search_fields = ("name",)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "project", "pre_answer")
    fieldsets = [
        (None, {"fields": [("question_text"), ("project"), ("pre_answer")]}),
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "answer_text")
    fieldsets = [
        (None, {"fields": [("question"), ("answer_text")]}),
    ]