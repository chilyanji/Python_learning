import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    search = input("Enter Company name: ")

    found = False

    for user in users:
        if search.lower() in user["address"]["city"].lower():
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['company']['name']}")
            print("-" * 30)
            found = True
            # break
            
    if not found:
        print(f"User not Found")


else:
    print(f"Error: {response.status_code}")




# Enter city: Gwenborough

# Output:
# Name: Leanne Graham
# Email: Sincere@april.biz
# Company: Romaguera-Crona