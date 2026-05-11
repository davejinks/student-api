# 🎓 Student Management API

A RESTful API built with **FastAPI** and **Pydantic v2** for managing student records.  
This is my first API project — built as part of my journey learning backend development as a Mechatronics Engineering student at **LASUSTECH**.

---

## 🚀 What I Learned Building This

- How to design and structure a **REST API** from scratch using FastAPI
- How **HTTP methods** map to real-world actions (GET → read, POST → create, PUT → update, DELETE → remove)
- How **path parameters** (`/student/{student_id}`) let you target specific resources in a URL
- How **Pydantic v2** validates incoming data automatically — if a field is the wrong type, FastAPI rejects the request before it even hits your function
- The difference between a **full model** (`Student`) and a **partial update model** (`UpdateStudent`) — using `Optional` fields with `exclude_unset=True` so only fields the client sends actually get updated
- How `model_copy(update=...)` lets you apply partial updates cleanly without overwriting untouched fields
- How **HTTPException** returns proper error codes (400 for bad input, 404 for not found) instead of crashing
- That in-memory storage (`dict`) is fast to build with but resets on every server restart — a real app would use a database like PostgreSQL or SQLite

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework for building the API |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation and schema definition |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server to run the app |

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/student-api.git
cd student-api
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

**5. Open the interactive docs**  
Visit → `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### Home
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns school info and API status |

### Student Operations
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/create-student/{student_id}` | Create a new student record |
| GET | `/get-student/{student_id}` | Retrieve a student by ID |
| PUT | `/update-student/{student_id}` | Update one or more fields of a student |
| DELETE | `/delete-student/{student_id}` | Delete a student record |
| GET | `/list-students` | List all students |

---

## 🧪 Example Usage

### Create a Student
**Request:**
```http
POST /create-student/1
Content-Type: application/json

{
  "name": "Akhabue Daniel",
  "age": 21,
  "major": "Mechatronics Engineering",
  "email": "daniel@example.com"
}
```
**Response:**
```json
{
  "message": "Student created successfully",
  "data": {
    "name": "Akhabue Daniel",
    "age": 21,
    "major": "Mechatronics Engineering",
    "email": "daniel@example.com"
  }
}
```

### Get a Student
```http
GET /get-student/1
```

### Update a Student (partial update supported)
```http
PUT /update-student/1
Content-Type: application/json

{
  "age": 22
}
```

### Delete a Student
```http
DELETE /delete-student/1
```

---

## 📁 Project Structure

```
student-api/
├── main.py            # All routes and models
├── requirements.txt   # Project dependencies
├── .gitignore         # Files excluded from Git
└── README.md          # This file
```

---

## ⚠️ Note on Storage

This project uses **in-memory storage** (a Python dictionary). All data is lost when the server restarts. This is intentional for simplicity — a future version will connect to a real database.

---

## 🔮 Planned Improvements

- [ ] Connect to a real database (SQLite → PostgreSQL)
- [ ] Add authentication (JWT tokens)
- [ ] Add search/filter to list-students endpoint
- [ ] Write automated tests with pytest

---

## 👤 Author

**Akhabue Daniel**  
Mechatronics Engineering Student — LASUSTECH  
📍 Lagos, Nigeria
