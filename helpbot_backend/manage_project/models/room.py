import random
import re
import threading
from datetime import datetime

from django.conf import settings
from django.db import models
from matrix_client.client import MatrixClient

from helpbot_backend.common.models import CreatedUpdatedDateModel

from .chat_bot import turn_on_chatbot


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
        print("waiting...")
        client = MatrixClient(settings.SERVER_URL)
        client.login(username=settings.MATRIX_USER, password=settings.MATRIX_PASSWORD)
        room = client.create_room(self.name, is_public=True)
        print("completed!")
        return dict(name=room.display_name, id=room.room_id)

    def save(self, *args, **kwargs):
        if not self.id_synapse:
            self.name = self.create_name()
            script = self.project.script_QA
            room_infor = self.create_room(self.name)
            self.id_synapse = room_infor["id"]
            chatbot_thread = threading.Thread(target=turn_on_chatbot, args=(room_infor["id"], script))
            chatbot_thread.start()
            super().save(*args, **kwargs)
