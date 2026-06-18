import requests
given_id = int(input("Please Enter Your ID: "))
given_name = input("Please Enter Your Name: ")
given_email = input("Please Enter Your Email: ")
given_age = int(input("Please Enter Your Age: "))

users = {
        "id": given_id,
        "name": given_name,
        "email": given_email,
        "age": given_age
}


response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=users
)
if response.status_code in [200, 201]:
    print("User Created Successfully")
else:
    print("Creation Failed")
    print(response.status_code)

created_user = response.json()

print(f"\n == Display returned data ==")
print(f"ID: {created_user['id']}")
print(f"Name: {created_user['name']}")
print(f"Email: {created_user['email']}")
print(f"Age: {created_user['age']}")