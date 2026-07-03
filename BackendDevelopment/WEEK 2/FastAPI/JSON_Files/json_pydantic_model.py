import requests

user = {
    "name": "John",
    "email": "john@example.com",
    "age": 25
}

response = requests.post(
    "http://127.0.0.1:8000/users",
    json=user
)

print("Status Code:", response.status_code)
print("Response:", response.json())