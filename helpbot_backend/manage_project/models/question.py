from django.db import models

from helpbot_backend.common.models import CreatedUpdatedDateModel


class Question(CreatedUpdatedDateModel):
    question_text = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey("manage_project.Project", on_delete=models.CASCADE, null=True, blank=True)
    pre_answer = models.ForeignKey(
        "manage_project.Answer", on_delete=models.CASCADE, null=True, blank=True, related_name="questions"
    )
