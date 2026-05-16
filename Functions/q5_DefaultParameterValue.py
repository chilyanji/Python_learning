# Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name = "User"):
    return f"Namaskar {name}"


name = str(input("Please enter your name: "))

if name == "":
    print(greet())
else:
    print(greet(name)) 
