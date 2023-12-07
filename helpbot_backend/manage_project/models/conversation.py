from django.db import models

from helpbot_backend.common.models import CreatedUpdatedDateModel


class Conversation(CreatedUpdatedDateModel):
    idx = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey("manage_project.Project", blank=True, null=True, on_delete=models.CASCADE)
