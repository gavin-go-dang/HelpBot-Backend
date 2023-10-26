from common.models import CreatedUpdatedDateModel
from django.db import models


class Message(CreatedUpdatedDateModel):
    content = models.CharField(max_length=50, blank=True, null=True)
    sender = models.CharField(max_length=100, blank=True, null=True)
    room = models.CharField(max_length=100, blank=True, null=True)
