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
                    "width": 212,
                    "height": 150,
                    "id": "node-1",
                    "type": "choiceUpdater",
                    "position": {"x": 150, "y": 100},
                    "data": {
                        "value": {"id": "node-1"},
                        "question": {
                            "question": {
                                "question": "What do you need? ",
                                "answer1": "Shoes ",
                                "answer2": "Rice",
                                "answer3": "Water",
                            },
                            "type": "choice",
                        },
                    },
                    "targetPosition": "left",
                    "sourcePosition": "right",
                    "selected": False,
                    "dragging": False,
                    "positionAbsolute": {"x": 150, "y": 100},
                },
                {
                    "width": 212,
                    "height": 150,
                    "id": "node-2",
                    "type": "textUpdater",
                    "position": {"x": 526, "y": -4.400000000000006},
                    "data": {"id": "node-2", "question": {"question": "How many pair you need?", "type": "text"}},
                    "targetPosition": "left",
                    "sourcePosition": "right",
                    "selected": False,
                    "positionAbsolute": {"x": 526, "y": -4.400000000000006},
                    "dragging": False,
                },
                {
                    "width": 212,
                    "height": 150,
                    "id": "node-3",
                    "type": "choiceUpdater",
                    "position": {"x": 842, "y": -14},
                    "data": {
                        "value": {"id": "node-3"},
                        "question": {
                            "question": {
                                "question": "What color do you need",
                                "answer1": "Baclk",
                                "answer2": "Red",
                                "answer3": "White",
                            },
                            "type": "choice",
                        },
                    },
                    "targetPosition": "left",
                    "sourcePosition": "right",
                    "selected": False,
                    "positionAbsolute": {"x": 842, "y": -14},
                    "dragging": False,
                },
                {
                    "width": 212,
                    "height": 150,
                    "id": "node-4",
                    "type": "textUpdater",
                    "position": {"x": 525, "y": 150},
                    "data": {"id": "node-4", "question": {"question": "How much?", "type": "text"}},
                    "targetPosition": "left",
                    "sourcePosition": "right",
                    "selected": False,
                    "positionAbsolute": {"x": 525, "y": 150},
                    "dragging": False,
                },
                {
                    "width": 212,
                    "height": 150,
                    "id": "node-5",
                    "type": "choiceUpdater",
                    "position": {"x": 519, "y": 317},
                    "data": {
                        "value": {"id": "node-5"},
                        "question": {
                            "question": {
                                "question": "What brand do you want to buy?",
                                "answer1": "Aqua",
                                "answer2": "Lavi",
                                "answer3": "H20",
                            },
                            "type": "choice",
                        },
                    },
                    "targetPosition": "left",
                    "sourcePosition": "right",
                    "selected": False,
                    "positionAbsolute": {"x": 519, "y": 317},
                    "dragging": False,
                },
            ],
            "edges": [
                {
                    "source": "node-1",
                    "sourceHandle": "b",
                    "target": "node-2",
                    "targetHandle": None,
                    "id": "reactflow__edge-node-1b-node-2",
                },
                {
                    "source": "node-2",
                    "sourceHandle": "b",
                    "target": "node-3",
                    "targetHandle": None,
                    "id": "reactflow__edge-node-2b-node-3",
                },
                {
                    "source": "node-1",
                    "sourceHandle": "c",
                    "target": "node-4",
                    "targetHandle": None,
                    "id": "reactflow__edge-node-1c-node-4",
                },
                {
                    "source": "node-1",
                    "sourceHandle": "d",
                    "target": "node-5",
                    "targetHandle": None,
                    "id": "reactflow__edge-node-1d-node-5",
                },
            ],
            "viewport": {"x": 247.8703885091909, "y": 51.808648794087446, "zoom": 0.8467453123625274},
        }

    def test_flow_to_script(self):
        json_input = self.generate_fake_json_input()
        result = flow_to_script(json_input)

        # Add assertions to check if the result is as expected
        self.assertIsInstance(result[0]["id"], str)
        self.assertIsInstance(result[0]["question"], str)
        self.assertIsInstance(result[0]["answer"], list)
        self.assertIsInstance(result[0]["next"], list)

        self.assertIsInstance(result[1]["id"], str)
        self.assertIsNone(result[1]["answer"])
        self.assertIsInstance(result[1]["next"], list)


if __name__ == "__main__":
    unittest.main()
