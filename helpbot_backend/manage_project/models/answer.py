from django.db import models

from helpbot_backend.common.models import CreatedUpdatedDateModel


class Answer(CreatedUpdatedDateModel):
    question = models.ForeignKey(
        "manage_project.Question", on_delete=models.CASCADE, null=True, blank=True, related_name="answers"
    )
    answer_text = models.CharField(null=True, blank=True, max_length=255)
