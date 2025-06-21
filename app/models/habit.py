from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class HabitBase(BaseModel):
    name: str
    frequency: List[str]  # e.g. ["Monday", "Wednesday"]


class HabitCreate(HabitBase):
    pass


class Habit(HabitBase):
    id: str
    created_at: Optional[datetime]
    logs: List[dict] = []

    class Config:
        orm_mode = True
