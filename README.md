# TaskFlow

A simple task management app I built to practice FastAPI and Docker. You can create tasks, set priorities and deadlines, and track progress through different status stages.

---

## What it does

- Register and login with JWT auth
- Add tasks with title, description, priority (low/medium/high), status, and deadline
- Filter tasks by status from the sidebar
- Deadlines turn yellow when due soon and red when overdue
- Stats at the top show a quick count of everything

---

## Stack

- **Backend** — FastAPI + SQLAlchemy
- **Database** — MySQL
- **Auth** — JWT with bcrypt password hashing
- **Frontend** — Bootstrap 5 (served via Jinja2 templates)
- **Deployment** — Docker + Docker Compose

