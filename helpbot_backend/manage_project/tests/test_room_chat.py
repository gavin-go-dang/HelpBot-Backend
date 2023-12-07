import pytest
from django.test import TestCase
from factory import SubFactory
from factory.django import DjangoModelFactory
from matrix_client.client import MatrixClient

from ..models import Room
from ..models.chat_bot import turn_on_chatbot
from .factories import ProjectFactory


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    name = "Test Room"
    id_synapse = "test_id_synapse"
    project = SubFactory(ProjectFactory)
    device = "Test Device"


class TestRoomView(TestCase):
    def setUp(self):
        self.room = RoomFactory()

    def test_create_name(self):
        name = self.room.create_name()
        assert name is not None

    def test_save(self):
        def mock_create_room(room_name, is_public=True):
            return type("Room", (), {"display_name": room_name, "room_id": "mocked_room_id"})

        def mock_turn_on_chatbot(room_id, script):
            pass

        with pytest.MonkeyPatch.context() as m:
            m.setattr(MatrixClient, "create_room", mock_create_room)
            m.setattr(turn_on_chatbot, "__call__", mock_turn_on_chatbot)

            self.room.save()

        assert self.room.id_synapse == "test_id_synapse"
