import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()
    print(f"Welcome To My Data Center")
    print("What way you choose to finding the required data")
    print(f"Search by Username: press 1")
    print(f"Search by Company: press 2")
    print(f"Search by City: press 3")

    option = int(input(f"Please Enter Your Choice: "))
    if option == 1:
        search = input("Enter Username: ")

        found = False

        for user in users:
            if search.lower() in user["username"].lower():
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
                print(f"Company: {user['company']['name']}")
                print("-" * 30)
                found = True
                break
                
        if not found:
            print(f"User not Found")
    elif option == 2:
        search = input("Enter Company name: ")

        found = False

        for user in users:
            if search.lower() in user["company"]["name"].lower():
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
                print(f"Company: {user['company']['name']}")
                print("-" * 30)
                found = True
                break
                
        if not found:
            print(f"User not Found")  
    elif option == 3:
        search = input("Enter City Name: ")

        found = False

        for user in users:
            if search.lower() in user["address"]["city"].lower():
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
                print(f"Company: {user['company']['name']}")
                found = True
                print("-" * 30)
                # break
                
        if not found:
            print(f"User not Found")

    else:
        print(f"Invalid Input")

else:
    print(f"Error: {response.status_code}")




# 1. Search by Username
# 2. Search by Company
# 3. Search by City

# Choose option: