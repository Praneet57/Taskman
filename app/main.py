from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import users, tasks

import time, sqlalchemy

for attempt in range(10):
    try:
        models.Base.metadata.create_all(bind=engine)
        print("✅ DB connected!")
        break
    except sqlalchemy.exc.OperationalError:
        print(f"⏳ DB not ready, retrying ({attempt+1}/10)...")
        time.sleep(3)

app = FastAPI(title="TaskFlow - Task Manager", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health():
    return {"status": "ok", "app": "TaskFlow"}
