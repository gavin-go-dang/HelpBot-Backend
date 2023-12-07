from django.test import TestCase
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Conversation, Project
from ..serializers import ProjectSerializers

fake = Faker()


class StyleConversationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(name=fake.word(), script_QA=fake.text())
        self.conversation = Conversation.objects.create(
            idx="20231204100622383547", room=fake.word(), project=self.project
        )

    def test_style_conversation(self):
        print(self.conversation.idx)
        response = self.client.get(
            "http://127.0.0.1:8000/api/v1/manage-project/style-conversation/20231204100622383547"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = ProjectSerializers(self.project)
        self.assertEqual(response.data, serializer.data)
