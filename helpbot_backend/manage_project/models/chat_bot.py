from datetime import datetime

from django.conf import settings
from matrix_client.client import MatrixClient

from .message import Message


def save_message(content, sender, room):
    new_message = Message(content=content, sender=sender, room=room)
    new_message.save()
    return "message was saved"


def turn_on_chatbot(room_id, script):
    homeserver_url = settings.SERVER_URL
    username = settings.HOMESERVER_USERNAME
    password = settings.HOMESERVER_PASSWORD
    print("0")
    print(room_id)
    # Khởi tạo client Matrix
    client = MatrixClient(homeserver_url)
    client.login(username=username, password=password)
    print("singed in")
    room = client.join_room(room_id)
    print("in room")
    # read json

    data = script
    questions = [item["question"] for item in data]
    answers = [item["answer"] for item in data]
    next_question = [item["next"] for item in data]

    def on_message(room, event):
        global current_question_id
        if event["type"] == "m.room.message":
            sender = event["sender"]
            message_body = event["content"]["body"]
            message = message_body.split(":")[-1]
            print(f"New message from {sender}: {message_body}")
            save_message(content=message_body, sender=sender, room=room_id)
            if event["content"]["body"] and username not in event["sender"]:
                now = datetime.now().strftime("%H:%M:%S")
                if message == "start":
                    current_question_id = 0
                    # room.send_text(
                    #     "{}-{}".format(now, questions[current_question_id]))
                else:
                    try:
                        if answers[current_question_id] and message in answers[current_question_id]:
                            current_question_id = next_question[current_question_id][
                                answers[current_question_id].index(message)
                            ]
                            room.send_text(f"{now}-{questions[current_question_id]}")
                            save_message(content=questions[current_question_id], sender="bot", room=room_id)
                        elif next_question[current_question_id]:
                            current_question_id = next_question[current_question_id]

                            room.send_text(f"{now}-{questions[current_question_id[0]]}")
                            if next_question[current_question_id]:
                                room.send_text("Your order was created successful")
                                save_message(content=questions[current_question_id[0]], sender="bot", room=room_id)
                    except NameError:
                        print(NameError)

    room.add_listener(on_message, event_type="m.room.message")

    client.start_listener_thread()

    input("Press Enter to stop...")

    client.logout()
