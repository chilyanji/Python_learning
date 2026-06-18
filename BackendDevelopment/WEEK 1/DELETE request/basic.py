import requests
user_id = input("Enter User ID to delete: ")
response = requests.delete(
    f"https://jsonplaceholder.typicode.com/users/{user_id}"
)

if response.status_code in [200, 201]:
    print("User Deleted Successfully")

else:
    print("Deletion Failed")