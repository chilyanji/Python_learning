words = ["banana", "apple", "cat"]
words.sort()
print(words)
words.sort(reverse=True)
print(words)
words.sort(key= lambda x: len(x))
print(words)


students = [
    ("Rahul", 80),
    ("Amit", 95),
    ("Neha", 70)
]

students.sort(key= lambda x: x[1])
print(students)