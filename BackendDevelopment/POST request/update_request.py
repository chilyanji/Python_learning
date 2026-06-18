import requests

given_id = int(input("Please Enter Your ID: "))
given_name = input("Please Enter Your Name: ")
given_email = input("Please Enter Your Email: ")


users = {
        "id": given_id,
        "name": given_name,
        "email": given_email
}

response = requests.put(
    f"https://jsonplaceholder.typicode.com/users/{given_id}",
    json=users
)

if response.status_code in [200, 201]:
    print("User Updated Successfully")
    updated_user = response.json()
    print(f"ID: {updated_user['id']}")
    print(f"Name: {updated_user['name']}")
    print(f"Email: {updated_user['email']}")
else:
    print("Updation Failed")
    print(response.status_code)
