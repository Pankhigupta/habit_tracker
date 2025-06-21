
markdown


# 📘 Habit Tracker API

A simple backend API built using **FastAPI** and **MongoDB** to help users track their daily or weekly habits. Users can create habits, log completions, view habit history, and delete habits.

---

## 🚀 API Endpoints

### 1. Create a Habit

- **Endpoint**: `POST /api/habits`
- **Description**: Creates a new habit.
- **Request Body**:
json
{
  "name": "Drink Water",
  "frequency": ["Monday", "Wednesday", "Friday"]
}
Response:

json


{
  "id": "60ef123...",
  "name": "Drink Water",
  "frequency": ["Monday", "Wednesday", "Friday"],
  "created_at": "2025-06-20T14:10:32Z",
  "logs": []
}
### 2. Get All Habits
Endpoint: GET /api/habits

Description: Returns a list of all habits.

Response:

json


[
  {
    "id": "60ef123...",
    "name": "Drink Water",
    "frequency": ["Monday", "Wednesday"],
    "created_at": "2025-06-20T14:10:32Z",
    "logs": []
  }
]
### 3. Log a Habit
Endpoint: POST /api/habits/{habit_id}/log

Description: Adds a log entry for a given date.

Query Params:

date (e.g. 2025-06-20)

completed (true or false)

Example:




POST /api/habits/60ef123abc/log?date=2025-06-20&completed=true
Response:

json


{
  "msg": "Log entry added"
}
### 4. Delete a Habit
Endpoint: DELETE /api/habits/{habit_id}

Description: Deletes a habit by ID.

Response:

json


{
  "msg": "Habit deleted"
}
🗄️ Database
This app uses MongoDB as the backend database. Habit logs and metadata are stored in a collection called habits.


⚙️ Environment Variables
Create a .env file in your root directory:




MONGO_URI=mongodb://localhost:27017
MONGO_DB=habit_tracker
💻 How to Run the Server



# 1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the FastAPI app
uvicorn app.main:app --reload
Open Swagger Docs: http://localhost:8000/docs

📦 Dependencies
Install manually:




pip install fastapi motor uvicorn pydantic python-dotenv
Or use:




pip install -r requirements.txt
✅ Sample cURL Commands
Create Habit



curl -X POST http://localhost:8000/api/habits \
-H "Content-Type: application/json" \
-d '{"name": "Read Book", "frequency": ["Monday", "Tuesday"]}'
Log Habit



curl -X POST "http://localhost:8000/api/habits/<habit_id>/log?date=2025-06-20&completed=true"
Get Habits



curl http://localhost:8000/api/habits
Delete Habit



curl -X DELETE http://localhost:8000/api/habits/<habit_id>
📌 Future Improvements
 Add user authentication (JWT)

 Track daily/weekly streaks

 Frontend UI with React or Flutter

 Daily reminders and analytics





