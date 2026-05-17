# Student Management System (CLI)


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print("-" * 30)


students = []


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = Student(roll_no, name, marks)
    students.append(student)

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        student.display()


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student.roll_no == roll_no:
            print("\nStudent Found:")
            student.display()
            return

    print("Student not found.\n")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    for student in students:
        if student.roll_no == roll_no:
            print("Enter new details")

            student.name = input("New Name: ")
            student.marks = float(input("New Marks: "))

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.\n")


# Run Program
menu()