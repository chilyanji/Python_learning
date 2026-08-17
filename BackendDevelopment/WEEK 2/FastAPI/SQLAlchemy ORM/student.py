from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional

from database import SessionLocal
from models import StudentDB

app = FastAPI()


# ---------------- Database ---------------- #

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- Schemas ---------------- #

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str
    phone: Optional[str] = None
    city: str
    state: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class StudentPublic(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


# ---------------- Routes ---------------- #
# ye hame students ki list dikhayega -- no password/phone/sensitive information
@app.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()

# ye shirf hame naam aur id dikayega
@app.get("/students/names", response_model=List[StudentPublic])
def get_student_names(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()

# ye create krega data matbl data upload krega

@app.post("/students", response_model=List[StudentResponse])
def create_students(
    students: List[Student],
    db: Session = Depends(get_db),
):
    created = []

    for student in students:

        # Check krega duplicate ID 
        if db.query(StudentDB).filter(StudentDB.id == student.id).first():
            raise HTTPException(
                status_code=400,
                detail=f"Student ID {student.id} already exists."
            )

        # Check  krega duplicate Email
        if db.query(StudentDB).filter(StudentDB.email == student.email).first():
            raise HTTPException(
                status_code=400,
                detail=f"Email '{student.email}' already exists."
            )
        # database me ye chize add hogi 
        db_student = StudentDB(
            id=student.id,
            name=student.name,
            age=student.age,
            email=student.email,
            phone=student.phone,
            city=student.city,
            state=student.state,
        )

        db.add(db_student)
        created.append(db_student)

    db.commit()

    for student in created:
        db.refresh(student)

    return created


@app.get("/students/{student_name}", response_model=Student)
def get_student(
    student_name: str,
    db: Session = Depends(get_db),
):
    student = (
        db.query(StudentDB)
        .filter(StudentDB.name == student_name)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student

# filter model
@app.get("/students/search", response_model=List[Student])
def search_students(
    q: str,
    db: Session = Depends(get_db),
):
    return (
        db.query(StudentDB)
        .filter(
            or_(
                StudentDB.name.ilike(f"%{q}%"),
                StudentDB.email.ilike(f"%{q}%"),
                StudentDB.city.ilike(f"%{q}%"),
                StudentDB.state.ilike(f"%{q}%"),
            )
        )
        .all()
    )

# student count 
@app.get("/students/count")
def student_count(
    db: Session = Depends(get_db),
):
    return {
        "total_students": db.query(StudentDB).count()
    }

# small update
@app.patch("/students/{student_name}", response_model=Student)
def update_student(
    student_name: str,
    updated: StudentUpdate,
    db: Session = Depends(get_db),
):
    student = (
        db.query(StudentDB)
        .filter(StudentDB.name == student_name)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    if updated.name is not None:
        student.name = updated.name

    if updated.age is not None:
        student.age = updated.age

    if updated.email is not None:
        student.email = updated.email

    if updated.phone is not None:
        student.phone = updated.phone

    if updated.city is not None:
        student.city = updated.city

    if updated.state is not None:
        student.state = updated.state

    db.commit()
    db.refresh(student)

    return student


@app.delete("/students/{student_name}")
def delete_student(
    student_name: str,
    db: Session = Depends(get_db),
):
    student = (
        db.query(StudentDB)
        .filter(StudentDB.name == student_name)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }