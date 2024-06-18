import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_post(title, body, userId):
    data = {
        "title": title,
        "body": body,
        "userId": userId
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    return response.json()
