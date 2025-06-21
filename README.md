📘 Habit Tracker API
A simple backend API built using FastAPI and MongoDB to help users track their habits. You can create habits, log completions, view habit history, and delete habits.

🚀 API Endpoints

1. Create a Habit
   Endpoint: POST /api/habits

Description: Creates a new habit.

Request Body:

json
Copy
Edit
{
"name": "Drink Water",
"frequency": ["Monday", "Wednesday", "Friday"]
}
Response:

json
Copy
Edit
{
"id": "60ef123...",
"name": "Drink Water",
"frequency": ["Monday", "Wednesday", "Friday"],
"created_at": "2025-06-20T14:10:32Z",
"logs": []
} 2. Get All Habits
Endpoint: GET /api/habits

Description: Returns a list of all habits.

Response:

json
Copy
Edit
[
{
"id": "60ef123...",
"name": "Drink Water",
"frequency": ["Monday", "Wednesday"],
"created_at": "2025-06-20T14:10:32Z",
"logs": [...]
}
] 3. Log a Habit
Endpoint: POST /api/habits/{habit_id}/log

Description: Adds a log entry for a given date.

Query Params:

date (YYYY-MM-DD)

completed (true/false)

Example:

bash
Copy
Edit
POST /api/habits/60ef123abc/log?date=2025-06-20&completed=true
Response:

json
Copy
Edit
{
"msg": "Log entry added"
} 4. Delete a Habit
Endpoint: DELETE /api/habits/{habit_id}

Description: Deletes a habit by ID.

Response:

json
Copy
Edit
{
"msg": "Habit deleted"
}
🗄️ Database
💾 MongoDB
The backend uses MongoDB to store all habit data.

Integration is done using the Motor async MongoDB driver.

🔌 Connection
Mongo URI is loaded from .env:

ini
Copy
Edit
MONGO_URI=mongodb://localhost:27017
MONGO_DB=habit_tracker
Configured in:

app/core/config.py

app/db/mongodb.py

💻 How to Run the Server

1. Clone the Repo
   bash
   Copy
   Edit
   git clone <repo_url>
   cd habit-tracker
2. Create a Virtual Environment
   bash
   Copy
   Edit
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install Dependencies
   bash
   Copy
   Edit
   pip install -r requirements.txt
4. Set Up Environment Variables
   Create a .env file:

ini
Copy
Edit
MONGO_URI=mongodb://localhost:27017
MONGO_DB=habit_tracker 5. Run the Server
bash
Copy
Edit
uvicorn app.main:app --reload
Visit docs at: http://localhost:8000/docs (Swagger UI)

🌐 (Optional) Frontend
If you're building a frontend (e.g. React), you can:

Start the React dev server: npm start

Make API requests to: http://localhost:8000/api/habits

Handle CORS if needed (already enabled via FastAPI defaults)

📬 Sample API Calls
✅ Create Habit (cURL)
bash
Copy
Edit
curl -X POST http://localhost:8000/api/habits \
 -H "Content-Type: application/json" \
 -d '{"name": "Read Book", "frequency": ["Monday", "Tuesday"]}'
📅 Log Habit
bash
Copy
Edit
curl -X POST "http://localhost:8000/api/habits/<habit_id>/log?date=2025-06-20&completed=true"
🔍 Get Habits
bash
Copy
Edit
curl http://localhost:8000/api/habits
❌ Delete Habit
bash
Copy
Edit
curl -X DELETE http://localhost:8000/api/habits/<habit_id>
📌 Technologies Used
FastAPI - API framework

Motor - Async MongoDB driver

Uvicorn - ASGI server

Pydantic - Data validation

Dotenv - Environment variable loading

✅ To Do / Extend
Add user authentication (JWT)

Track streaks or completion %

Add frontend UI (React/Flutter)

Export habit logs
