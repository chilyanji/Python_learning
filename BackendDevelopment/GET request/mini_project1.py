import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    users = sorted(users, key=lambda user: user["name"])

    def display_user(user):
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print(f"Company: {user['company']['name']}")
        print("-" * 30)

    print("\n=== All Users (A-Z) ===")

    for user in users:
        print(user["name"])
    
    print("\n=== User Data Center ===")
    print("1. Search by Username")
    print("2. Search by Company")
    print("3. Search by City")

    while True:
        try:
            option = int(input("Please Enter Your Choice: "))
            if option in [1, 2, 3]:
                break
            print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")
    print("-" * 30)
    
    
    found = False
    matches = 0

    if option == 1:
        search = input("Enter Username: ")

        for user in users:
            if search.lower() in user["username"].lower():
                display_user(user)
                found = True
                # break
                
        if not found:
            print(f"User not Found")
    elif option == 2:
        search = input("Enter Company name: ")

        for user in users:
            if search.lower() in user["company"]["name"].lower():
                display_user(user)
                found = True
                matches += 1
                # break
        print(f"Found {matches} matching users")       
        if not found:
            print(f"User not Found")  
    elif option == 3:
        search = input("Enter City Name: ")

        for user in users:
            if search.lower() in user["address"]["city"].lower():
                display_user(user)
                matches += 1
                found = True
        print(f"Found {matches} matching users")
                
        if not found:
            print(f"User not Found")

else:
    print(f"Error: {response.status_code}")




# 1. Search by Username
# 2. Search by Company
# 3. Search by City

# Choose option: