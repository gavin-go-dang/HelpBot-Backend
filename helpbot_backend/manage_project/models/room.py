import random
from datetime import datetime

from common.models import CreatedUpdatedDateModel
from django.db import models

from ..create_room import create_room


class Room(CreatedUpdatedDateModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    id_synapse = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey("manage_project.Project", on_delete=models.CASCADE, null=True, blank=True)
    device = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        num = random.random()
        now = datetime.now()
        room_infor = create_room("{}{}{}".format(self.project.name.replace(" ", ""), now.strftime("%H%M%S"), num))
        self.id_synapse = room_infor["id"]
        self.name = room_infor["name"]
        super().save(*args, **kwargs)
