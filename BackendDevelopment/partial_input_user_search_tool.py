import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    search = input("Enter Company name: ")

    found = False

    for user in users:
        if search.lower() in user["company"]["name"].lower():
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)
            found = True
            # break
            
    if not found:
        print(f"User not Found")


else:
    print(f"Error: {response.status_code}")



# Enter company: Hoeger or LLC

# Output:
# Name: Clementina DuBuque
# Email: Rey.Padberg@karina.biz
# City: Lebsackbury
