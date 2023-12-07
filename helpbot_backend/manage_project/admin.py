from django.contrib import admin

from .models import Answer, Message, Project, Question, Room


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at")
    fieldsets = [
        (
            None,
            {
                "fields": [
                    ("name"),
                    ("owner"),
                    ("script_QA"),
                    ("flow_chart"),
                    ("style_widget"),
                    ("avt_img"),
                    ("secretkey"),
                ]
            },
        ),
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
        (None, {"fields": [("id"), ("question_text"), ("project"), ("pre_answer")]}),
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "answer_text", "updated_at", "created_at")
    fieldsets = [
        (None, {"fields": [("question"), ("answer_text"), ("updated_at"), ("created_at")]}),
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("content", "sender", "room", "updated_at", "created_at")
    fieldsets = [(None, {"fields": [("content"), ("sender"), ("room"), ("conversation")]})]
