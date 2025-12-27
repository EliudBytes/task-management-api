# 📝 Task Management API

A Django REST Framework API for managing tasks with JWT authentication, filtering, and interactive Swagger documentation.  
This project is designed to be simple, secure, and production‑ready, making it a great starting point for backend development and deployment.

---

## 🚀 Features
- 🔐 **JWT Authentication** (login, refresh, secure endpoints)
- 📋 **CRUD Operations** for tasks (create, read, update, delete)
- 🔎 **Filtering & Ordering** support for tasks
- 📖 **Interactive API Docs** powered by drf‑spectacular (Swagger/OpenAPI)
- 🛠 **Admin Panel** for managing users and tasks
- 🌐 **Deployment‑ready** with Render/Heroku configuration

---

## 🛠 Tech Stack
- **Backend:** Django 6.0, Django REST Framework
- **Auth:** SimpleJWT
- **Docs:** drf‑spectacular
- **Database:** SQLite (local), PostgreSQL (production)
- **Deployment:** Render (recommended free platform)

---

## ⚙️ Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api

# Create and activate venv
python -m venv venv
.\venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
