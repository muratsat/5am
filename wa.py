import requests

from config import env

HEADERS = {"Content-Type": "application/json", "x-api-key": env.WA_API_KEY}


def send_message(chat_id: str, message: str) -> tuple[str, str] | None:
    print(f"Sending message to {chat_id}: ", end="")

    if chat_id.find("@g.us") != -1:
        raise Exception("Group chat id is not supported")

    if chat_id.find("@c.us") == -1:
        chat_id = f"{chat_id}@c.us"

    url = f"{env.WA_API_URL}/client/sendMessage/{env.WA_SESSION_ID}"

    data = {
        "chatId": chat_id,
        "contentType": "string",
        "content": message,
    }

    response = requests.post(url=url, json=data, headers=HEADERS)

    print("Ok" if response.status_code == 200 else "Failed")
