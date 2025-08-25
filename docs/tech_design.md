# Tech Design Document

## High-Level Architecture
- **Frontend (React.js):** User interface for dashboard, metrics, and build list
- **Backend (FastAPI):** Serves REST API, handles build data, metrics, and notifications
- **Database (PostgreSQL):** Stores build execution records
- **Email Notification:** Backend triggers email on pipeline failure
- **Docker Compose:** Orchestrates all services

```
[User] <-> [React Frontend] <-> [FastAPI Backend] <-> [PostgreSQL DB]
                                 |
                                 +--[Gmail SMTP]
```

## API Structure
### Routes
- `GET /metrics/summary` — Returns pipeline metrics
  - **Sample Response:**
    ```json
    {
      "total": 10,
      "success": 7,
      "failure": 3,
      "avg_time": 110.5,
      "last_status": "Success"
    }
    ```
- `GET /builds/` — List all builds
  - **Sample Response:**
    ```json
    [
      {
        "id": 1,
        "pipeline": "GitHub Actions",
        "status": "Success",
        "build_time": 120,
        "timestamp": "2025-08-25 10:00",
        "success": true
      },
      ...
    ]
    ```
- `POST /builds/` — Create a new build (triggers email if failed)

## DB Schema
- **Build Table:**
  - `id` (int, primary key)
  - `pipeline` (str)
  - `status` (str)
  - `build_time` (float)
  - `timestamp` (datetime)
  - `success` (bool)

## UI Layout (Explanation)
- **Dashboard:**
  - Metric cards for total builds, success, failure, average build time, last status
  - Bar chart for success vs failure
- **Build List:**
  - Table of build executions with details
- **Notification:**
  - Email sent to configured recipient on pipeline failure
