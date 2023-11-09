import factory
from factory.django import DjangoModelFactory

from ....manage_project.models import Project


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Faker("word")
    owner = factory.Faker("name")
    chatbot = factory.Faker("name")
    script_QA = factory.Faker("json")
    flow_chart = factory.Faker("json")
    style_widget = factory.Faker("json")
