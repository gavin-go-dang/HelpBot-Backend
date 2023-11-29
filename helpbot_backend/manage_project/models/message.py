from django.db import models

from helpbot_backend.common.models import CreatedUpdatedDateModel


class Message(CreatedUpdatedDateModel):
    content = models.CharField(max_length=255, blank=True, null=True)
    sender = models.CharField(max_length=100, blank=True, null=True)
    room = models.CharField(max_length=100, blank=True, null=True)
    conversation = models.CharField(default="", null=True, blank=True)
