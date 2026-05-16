# Dictionaries are used to store data values in key:values pair They are unordered, mutable(changeable)& don't allow duplicate keys//

info = {
    "name" : "Ayush",
    "Village" : "Yarpur",
    "age" : 21,
    "subjects" : ["python", "C", "javaScript", "C++"],
    "is_adult" : True,
    "marks" : 95.5,
    1 : "A",
}

print(type(info))
print(info["name"])
print(info["age"])
info["name"] = "Saurabh"
print(info)

for information in info:
    print(information)