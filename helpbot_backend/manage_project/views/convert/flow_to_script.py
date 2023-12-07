import json


def flow_to_script(JSON1):
    list_chain = []

    def get_question(node):
        # breakpoint()
        if node["type"] == "choiceUpdater":
            return node["data"]["question"]["question"]["question"]
        else:
            return node["data"]["question"]["question"]

    def get_answer(node):
        if node["type"] == "choiceUpdater":
            return [
                node["data"]["question"]["question"]["answer1"],
                node["data"]["question"]["question"]["answer2"],
                node["data"]["question"]["question"]["answer3"],
            ]

        else:
            return None

    def get_next(node, edges):
        next = []
        for edge in edges:
            if edge["source"] == node["id"]:
                next.append(edge["target"])
        return next

    for node in JSON1["nodes"]:
        list_chain.append(
            {
                "id": node["id"],
                "question": get_question(node),
                "answer": get_answer(node),
                "next": get_next(node, JSON1["edges"]),
            }
        )

    index_dict = {item["id"]: idx for idx, item in enumerate(list_chain)}

    for item in list_chain:
        item["next"] = [index_dict[node_id] for node_id in item["next"]]

    return list_chain
