# ✅ ToDo API – FastAPI CRUD Project

A simple and clean REST API for managing tasks (ToDo items), built with FastAPI, SQLite and SQLAlchemy.  
Tested with Pytest, documented with Swagger, and ready for production enhancements.

---

## 🚀 Features

- 📌 Full CRUD support (`Create`, `Read`, `Update`, `Delete`)
- 🧠 Data validation with Pydantic
- 🧪 Automated tests with Pytest
- 🔍 Interactive docs via Swagger UI
- 🛠️ Modular and scalable project structure

---

## 📂 Project Structure

todo_app/
├── main.py
├── database.py
├── models/
│ └── task.py
├── schemas/
│ └── task.py
├── crud/
│ └── task.py
├── routers/
│ └── task.py
├── tests/
│ └── test_main.py
└── todo.db

---

## 🧪 Running the Tests

```bash
pytest tests/
```

📦 Requirements
Python 3.12+

FastAPI

Uvicorn

SQLAlchemy

Pydantic

Pytest

Httpx

You can install all with:
```bash
pip install -r requirements.txt
```

▶️ How to Run Locally
Clone the repository

Create a virtual environment

Install dependencies

Run the API:

```bash
uvicorn main:app --reload
```

Access the docs at:

http://localhost:8000/docs

🧠 Future Improvements
Dockerization and cloud deployment

JWT authentication

Alembic migrations

CI pipeline

Made with 💻 by Daniel Pedroso (aka Amon)

