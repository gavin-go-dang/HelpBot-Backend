import random
import re
from datetime import datetime

from common.models import CreatedUpdatedDateModel
from django.conf import settings
from django.db import models
from matrix_client.client import MatrixClient


class Room(CreatedUpdatedDateModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    id_synapse = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey("manage_project.Project", on_delete=models.CASCADE, null=True, blank=True)
    device = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def create_name(self):
        num = random.randint(0, 100)
        now = datetime.now().strftime("%H%M%S")
        project = self.project
        name = f"{project}{now}{num}"
        return re.sub(r"[^a-zA-Z0-9]", "", name)

    def create_room(self, name):
        client = MatrixClient(settings.SERVER_URL)
        client.login(username=settings.MATRIX_USER, password=settings.MATRIX_PASSWORD)
        room = client.create_room(self.name, is_public=True)
        return dict(name=room.display_name, id=room.room_id)

    def save(self, *args, **kwargs):
        if not self.id_synapse:
            self.name = self.create_name()

            room_infor = self.create_room(self.name)
            self.id_synapse = room_infor["id"]

            super().save(*args, **kwargs)
