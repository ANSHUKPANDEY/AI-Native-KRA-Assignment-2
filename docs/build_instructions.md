# Build Instructions for CI/CD Health Dashboard Application

## Prerequisites
- Docker and Docker Compose installed
- (Optional) Node.js and Python for local development

## Steps to Build and Run the Application

### 1. Clone the Repository
```
git clone <repo-url>
cd AI-Native-KRA-Assignment-2
```

### 2. Build and Start the Application Using Docker Compose
```
docker compose up --build
```
This command will:
- Build the backend (FastAPI) and frontend (React) containers
- Start the PostgreSQL database and initialize the schema
- Start all services in the background

### 3. Access the Application
- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **Backend API:** [http://localhost:8000](http://localhost:8000)

### 4. Stopping the Application
```
docker compose down
```

### 5. (Optional) Local Development
#### Backend
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
#### Frontend
```
cd frontend
npm install
npm start
```

### 6. Database Initialization
- The database schema is automatically initialized from `db/schema/init.sql` when the database container starts.

---
For troubleshooting, check container logs:
```
docker compose logs backend
```
```
docker compose logs frontend
```
```
docker compose logs db
```
