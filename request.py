import requests

url = "http://localhost:8000/api/messages/"
data = {
    "date": "2025-05-22",
    "time": "19:54", 
    "message": "message display here!"
}
response = requests.post(url, json=data)
print(response.json())
