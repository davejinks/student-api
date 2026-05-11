from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import Optional

app = FastAPI(
    title="Student Management API",
    description="A simple CRUD API for managing student records at LASUSTECH.",
    version="1.0.0"
)


class Student(BaseModel):
    name: str
    age: int
    major: str
    email: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Akhabue Daniel",
                "age": 21,
                "major": "Mechatronics Engineering",
                "email": "daniel@example.com"
            }
        }
    )


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    major: Optional[str] = None
    email: Optional[str] = None


students = {}


@app.get("/")
async def school_home():
    return {
        "school_name": "LASUSTECH",
        "department": "Mechatronics Engineering",
        "status": "Online"
    }


@app.post("/create-student/{student_id}")
async def create_student(student_id: int, student: Student):
    if student_id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[student_id] = student
    return {"message": "Student created successfully", "data": students[student_id]}


@app.get("/get-student/{student_id}")
async def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.put("/update-student/{student_id}")
async def update_student(student_id: int, student_update: UpdateStudent):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    existing_student = students[student_id]
    update_data = student_update.model_dump(exclude_unset=True)
    updated_student = existing_student.model_copy(update=update_data)

    students[student_id] = updated_student

    return {"message": "Student updated", "data": students[student_id]}


@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student successfully deleted"}


@app.get("/list-students")
async def list_students():
    return [{"student_id": sid, **s.model_dump()} for sid, s in students.items()]
