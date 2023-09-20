import os
import random
from datetime import datetime

from common.models import CreatedUpdatedDateModel
from django.db import models
from dotenv import load_dotenv
from matrix_client.client import MatrixClient

load_dotenv()


class Room(CreatedUpdatedDateModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    id_synapse = models.CharField(max_length=50, blank=True, null=True)
    project = models.ForeignKey("manage_project.Project", on_delete=models.CASCADE, null=True, blank=True)
    device = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def create_room(self, name):
        client = MatrixClient(os.getenv("SERVER_URL"))
        client.login(username=os.getenv("MATRIX_USER"), password=os.getenv("MATRIX_PASSWORD"))
        room = client.create_room(self.name, is_public=True)
        print("Public room created with ID:", room.room_id)
        return dict(name=room.display_name, id=room.room_id)

    def save(self, *args, **kwargs):
        num = random.random()
        now = datetime.now()
        room_infor = self.create_room("{}{}{}".format(self.project.name.replace(" ", ""), now.strftime("%H%M%S"), num))
        self.id_synapse = room_infor["id"]
        self.name = room_infor["name"]
        super().save(*args, **kwargs)
