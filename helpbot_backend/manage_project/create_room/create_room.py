import os

from dotenv import load_dotenv
from matrix_client.client import MatrixClient

load_dotenv()


def create_room(name):
    client = MatrixClient(os.getenv("SERVER_URL"))
    client.login(username=os.getenv("MATRIX_USER"), password=os.getenv("MATRIX_PASSWORD"))
    room = client.create_room(name, is_public=True)
    print("Public room created with ID:", room.room_id)
    return dict(name=room.display_name, id=room.room_id)
