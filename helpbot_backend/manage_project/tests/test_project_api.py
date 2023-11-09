from django.test import TestCase
from faker import Faker

from ..models import Project
from ..models.project import generate_random_string
from ..tests.factories import ProjectFactory

faker = Faker()


class ProjectAPITestCase(TestCase):
    def setUp(self):
        self.project = ProjectFactory()

    def test_project_creation(self):
        self.assertTrue(isinstance(self.project, Project))
        self.assertIsNotNone(self.project.name)
        self.assertIsNotNone(self.project.owner)
        # Add more assertions as needed

    def test_generate_random_string(self):
        key_random_len = 15
        random_string = generate_random_string()
        self.assertTrue(random_string.startswith("CHATBOT_KEY"))
        self.assertEqual(len(random_string), len("CHATBOT_KEY") + key_random_len)
