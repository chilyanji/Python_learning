# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")

# print("Status Code:", response.status_code)
# print(response.json())
# users = response.json()
# for user in users:
#     # print("Name: ", user["name"])
#     # print("Username: ", user["username"])
#     # print("Email: ", user["email"])
#     print(user["name"], "-", user["username"], "-", user["email"])
# for user in users:
#     print(user["company"]["name"])
# for user in users:
#     # print(f"{user['id']} - {user['name']} - {user['email']}")
#     print(f"{user['name']} works at  {user['company']['name']}")


# 1 - Leanne Graham - Sincere@april.biz
# print(f"Total number of Users: {len(users)}")

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
# users = response.json()
if response.status_code == 200:
    users = response.json()
    for user in users:
        # print(f"{user['id']} - {user['name']} - {user['email']}")
        # print(f"{user['name']} works at  {user['company']['name']}")
        # print(f"{user['name']} lives in  {user['address']['city']}")
        print(f"{user['name']} | " 
            f"{user['email']} | "
            f"{user['address']['city']} | " 
            f"{user['company']['name']}"
            )
else:
    print(f"Error: {response.status_code}")