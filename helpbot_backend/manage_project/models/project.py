from common.models import CreatedUpdatedDateModel
from django.db import models


class Project(CreatedUpdatedDateModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    chatbot = models.CharField(max_length=100, blank=True, null=True)
    script_QA = models.JSONField(null=True, blank=True)
    flow_chart = models.JSONField(null=True, blank=True)
    style_widget = models.JSONField(null=True, blank=True)
    avt_img = models.ImageField(upload_to="project_img/", null=True, blank=True)
    secretkey = models.CharField(max_length=50, null=True, blank=True)
