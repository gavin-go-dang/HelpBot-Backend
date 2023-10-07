from common.models import CreatedUpdatedDateModel
from django.db import models


class Project(CreatedUpdatedDateModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    chatbot = models.CharField(max_length=100, blank=True, null=True)
    script_QA = models.JSONField(null=True, blank=True)
