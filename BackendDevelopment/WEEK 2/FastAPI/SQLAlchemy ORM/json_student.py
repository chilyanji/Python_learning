import requests

user = [
    {
        "id": 1,
        "name": "Ayush",
        "email": "ayush@example.com",
        "age": 22,
        "phone": "9548860936",
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    },
    {
        "id": 2,
        "name": "Aditya",
        "email": "aditya@example.com",
        "age": 20,
        "phone": "9690876767",
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    },
    {
        "id": 3,
        "name": "Abhayraj",
        "email": "abhayraj@example.com",
        "age": 25,
        "phone": "8126028826",
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    },
    {
        "id": 4,
        "name": "Chirag",
        "email": "chirag@example.com",
        "age": 20,
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    },
    {
        "id": 5,
        "name": "Arnav",
        "email": "arnav@example.com",
        "age": 18,
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    },
    {
        "id": 6,
        "name": "Nihar",
        "email": "nihar@example.com",
        "age": 18,
        "city": "Thana Bhawan",
        "state": "Uttar Pradesh"
    }
]

response = requests.post(
    "http://127.0.0.1:8000/students",
    json=user
)
print("Status Code:", response.status_code)

