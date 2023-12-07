from django.test import TestCase

from ..models import Message
from ..models.chat_bot import save_message


class SaveMessageTestCase(TestCase):
    def test_save_message(self):
        room = "test_room"
        sender = "test_sender"
        conversation = "id_conversation"

        # Call the function
        result = save_message("Test content", sender, room, conversation)

        saved_message = Message.objects.last()
        self.assertIsNotNone(saved_message)
        self.assertEqual(saved_message.content, "Test content")
        self.assertEqual(saved_message.sender, sender)
        self.assertEqual(saved_message.room, room)
        self.assertEqual(saved_message.conversation, conversation)

        # Check if the function returns the correct message
        self.assertEqual(result, "message was saved")
