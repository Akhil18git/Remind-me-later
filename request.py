import requests

BASE_URL = "http://localhost:8000/"
ENDPOINT = "api/messages/"
data = {
    "date": "2025-05-22",
    "time": "19:54", 
    "message": "message display here!"
}
response = requests.post(BASE_URL + ENDPOINT, json=data)
print(response.json())
