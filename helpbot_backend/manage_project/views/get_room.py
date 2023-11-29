import json
import re
import threading
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation
from ..models.chat_bot import turn_on_chatbot
from ..models.project import Project


def save_conversation(idx_conv, room, project):
    new_conversation = Conversation(idx=idx_conv, room=room, project=project)
    new_conversation.save()
    return "Conversation was saved"


class GetRoomChat(APIView):
    id_room_list = [
        "!HHOPNJjwesQIkTpVep:chat.studying.id.vn",
        "!XgToJCePFeDiAEUyJk:chat.studying.id.vn",
        "!dxHWYvfVNzsSSsxObJ:chat.studying.id.vn",
        "!pNfsswYmSodwErCqge:chat.studying.id.vn",
        "!ygcPVcOfGxcrXpcYKB:chat.studying.id.vn",
        "!rAAalhoguZgbdonBII:chat.studying.id.vn",
        "!ZbvXtsvOSEMELSvxyP:chat.studying.id.vn",
        "!FoCzBMkGvlQqpdVikg:chat.studying.id.vn",
        "!FGgzNjIbomnCpWsXQI:chat.studying.id.vn",
        "!XaCKuqJEQbnwdVXDDC:chat.studying.id.vn",
        "!eERCdQCBIVIGWiqlzN:chat.studying.id.vn",
    ]
    path_id_file = "helpbot_backend//manage_project/views/id_room_available.txt"

    def get(self, request, id):
        try:
            with open(self.path_id_file) as f:
                id_list_tx = f.read()

            id_list = json.loads(id_list_tx)
            if not id_list:
                id_list = self.id_room_list
            id_room = id_list.pop()
            id_conversation = re.sub(r"[^\d]", "", str(datetime.now()))
            project = Project.objects.get(id=id)
            save_conversation(idx_conv=id_conversation, room=id_room, project=project)

            chatbot_thread = threading.Thread(
                target=turn_on_chatbot, args=(id_room, project.script_QA, id_conversation)
            )
            chatbot_thread.start()

            with open(self.path_id_file, "w") as f:
                json.dump(id_list, f)

            return Response({"id": id_room}, status=status.HTTP_200_OK)

        except FileNotFoundError:
            return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
