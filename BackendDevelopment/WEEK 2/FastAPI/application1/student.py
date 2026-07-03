from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

students = []

class Address(BaseModel):
    city: str
    state: str

class AddressUpdate(BaseModel):
    city: Optional[str] = None
    state: Optional[str] = None
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[AddressUpdate] = None
class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str
    address: Address
    phone: Optional[str] = None


@app.post("/students")
def create_users(new_users: List[Student]):
    students.extend(new_users)
    return {
        "students": students,
        "message": f"{len(new_users)} users added"
    }

@app.get("/students") 
def get_students():
    return students

@app.get("/students/search")
def search_students(q: str):
    results = []

    for student in students:
        if (
            q.lower() in student.name.lower()
            or q.lower() in student.email.lower()
            or q.lower() in student.address.city.lower()
            or q.lower() in student.address.state.lower()
            or (student.phone and q.lower() in student.phone.lower())
        ):
            results.append(student)

    if not results:
        return {"message": "No students found"}

    return results


@app.get("/students/count")
def get_students_count():
    return {
        "total_students": len(students)
    }


@app.patch("/students/{student_name}")
def update_student(student_name: str, updated_data: StudentUpdate):
    for student in students:
        if student.name == student_name:

            if updated_data.name is not None:
                student.name = updated_data.name

            if updated_data.age is not None:
                student.age = updated_data.age

            if updated_data.email is not None:
                student.email = updated_data.email

            if updated_data.phone is not None:
                student.phone = updated_data.phone

            if updated_data.address is not None:
                if updated_data.address.city is not None:
                    student.address.city = updated_data.address.city
                if updated_data.address.state is not None:
                    student.address.state = updated_data.address.state

            return {
                "message": "Student updated successfully",
                "student": student
            }

    return {"message": "Student not found"}

@app.delete("/students/delete_student")
def delete_student(student_name: str):
    for i, student in enumerate(students):
        if student.name == student_name:
            deleted_student = students.pop(i)
            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    return {
        "message": "Student not found"
    }

@app.get("/students/{student_name}")
def get_student(student_name: str):
    for student in students:
        if student.name == student_name:
            return student

    return {
        "message": "Student not found"
    }

