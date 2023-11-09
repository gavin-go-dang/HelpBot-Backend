import unittest

from faker import Faker

from ..views.convert.flow_to_script import flow_to_script


class TestFlowToScript(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def generate_fake_json_input(self):
        return {
            "nodes": [
                {
                    "id": 1,
                    "type": "choiceUpdater",
                    "data": {
                        "question": f"""{{"question": {{"question": "{self.fake.sentence()}",
                        "answer1": "{self.fake.sentence()}",
                        "answer2": "{self.fake.sentence()}",
                        "answer3": "{self.fake.sentence()}"}}}}"""
                    },
                },
                {
                    "id": 2,
                    "type": "otherType",
                    "data": {"question": f'{{"question": {{"question": "{self.fake.sentence()}"}}}}'},
                },
            ],
            "edges": [
                {"source": 1, "target": 2},
            ],
        }

    def test_flow_to_script(self):
        json_input = self.generate_fake_json_input()

        result = flow_to_script(json_input)

        # Add assertions to check if the result is as expected
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0]["id"], int)
        self.assertIsInstance(result[0]["question"], str)
        self.assertIsInstance(result[0]["answer"], list)
        self.assertIsInstance(result[0]["next"], list)

        self.assertIsInstance(result[1]["id"], int)
        self.assertIsInstance(result[1]["question"]["question"], str)
        self.assertIsNone(result[1]["answer"])
        self.assertIsInstance(result[1]["next"], list)


if __name__ == "__main__":
    unittest.main()
