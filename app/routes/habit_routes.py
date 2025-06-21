from fastapi import APIRouter, HTTPException
from app.models.habit import HabitCreate
from app.db.mongodb import habit_collection
from datetime import datetime
from bson import ObjectId

router = APIRouter()

# 1. Create Habit


@router.post("/habits")
async def create_habit(habit: HabitCreate):
    habit_data = habit.dict()
    habit_data["created_at"] = datetime.utcnow()
    habit_data["logs"] = []
    result = await habit_collection.insert_one(habit_data)
    return {"id": str(result.inserted_id), **habit_data}

# 2. Get All Habits


@router.get("/habits")
async def get_habits():
    habits = []
    cursor = habit_collection.find()
    async for habit in cursor:
        habit["id"] = str(habit["_id"])
        del habit["_id"]
        habits.append(habit)
    return habits

# 3. Log Habit (e.g. completed: true/false)


@router.post("/habits/{habit_id}/log")
async def log_habit(habit_id: str, date: str, completed: bool):
    try:
        habit_obj_id = ObjectId(habit_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = await habit_collection.update_one(
        {"_id": habit_obj_id},
        {"$push": {"logs": {"date": date, "completed": completed}}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"msg": "Log entry added"}

# 4. Delete Habit


@router.delete("/habits/{habit_id}")
async def delete_habit(habit_id: str):
    try:
        habit_obj_id = ObjectId(habit_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = await habit_collection.delete_one({"_id": habit_obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"msg": "Habit deleted"}
