import requests

def display_user(user):
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"City: {user['address']['city']}")
    print(f"Company: {user['company']['name']}")
    print("-" * 30)

print("\n=== Welcome To User Data Center ===")
print("1. Create new user")
print("2. Read User Profile")
print("3. Update User Data")
print("4. Delete User")
print("5. Exit")

while True:
        try:
            main_option = int(input("Please Enter Your Choice: "))
            if main_option in [1, 2, 3, 4]:
                break
            print("Please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number.")
print("-" * 30)

if main_option == 1:
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
    print(f"ID: {created_user['id']}")
    print(f"Name: {created_user['name']}")
    print(f"Email: {created_user['email']}")
    print(f"Age: {created_user['age']}")
elif  main_option == 2:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        users = response.json()
        users = sorted(users, key=lambda user: user["name"])

        

        print("\n=== All Users (A-Z) ===")

        for user in users:
            print(user["name"])
        
        print("\n=== User Data Center ===")
        print("1. Search by Username")
        print("2. Search by Company")
        print("3. Search by City")

        while True:
            try:
                search_option = int(input("Please Enter Your Choice: "))
                if search_option in [1, 2, 3]:
                    break
                print("Please choose 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        print("-" * 30)
        
        
        found = False
        matches = 0

        if search_option == 1:
            search = input("Enter Username: ")

            for user in users:
                if search.lower() in user["username"].lower():
                    display_user(user)
                    found = True
                    matches += 1
                    # break
            print(f"Found {matches} matching users")      
            if not found:
                print(f"User not Found")
        elif search_option == 2:
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
        elif search_option == 3:
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


elif main_option == 3:
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


elif main_option == 4:
    user_id = input("Enter User ID to delete: ")
    response = requests.delete(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    if response.status_code in [200, 204]:
        print("User Deleted Successfully")

    else:
        print("Deletion Failed")

if main_option == 5:
    print("Goodbye!")
    exit()
