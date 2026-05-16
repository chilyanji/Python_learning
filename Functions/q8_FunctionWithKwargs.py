# Create a function that accepts any number of keywards arguments and print them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Ayush", Surname="Kumar")
print_kwargs(name="Ayush", Surname="Kumar", college = "MMMUT")
print_kwargs(name="Ayush Singh")