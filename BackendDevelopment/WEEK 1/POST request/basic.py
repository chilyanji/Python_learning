import requests


users = [
    {
        "name": "John",
        "email": "john@example.com",
        "id": 11,
        "age": 25
    },
    {
        "name": "Alice",
        "email": "alice@example.com",
        "id": 12,
        "age": 24
    },
    {
        "name": "Bob",
        "email": "bob@example.com",
        "id": 13,
        "age": 26
    },
    {
    "name": "Ayush Singh",
    "email": "ayush@example.com",
    "id": 14,
    "age": 22
    }
]

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=users
)
if response.status_code in [200, 201]:
    print("User Created")
else:
    print("Creation Failed")

print(response.json())