from fastapi import FastAPI
from app.routes.habit_routes import router as habit_router

app = FastAPI(title="Habit Tracker API")

app.include_router(habit_router, prefix="/api")
