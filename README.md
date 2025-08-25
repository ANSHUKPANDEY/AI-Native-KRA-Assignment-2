# CI/CD Pipeline Health Dashboard

## Application Architecture Summary

This project is a 3-tier web application for monitoring CI/CD pipeline executions. It provides a real-time dashboard to visualize pipeline metrics, list build executions, and send email notifications on failures. The application is fully containerized using Docker Compose.

**Architecture Overview:**
- **Frontend (React.js):** User interface for dashboard and build list
- **Backend (FastAPI):** REST API for metrics, builds, and notifications
- **Database (PostgreSQL):** Stores build execution records
- **Email Notification:** Sends email to configured recipient on pipeline failure
- **Docker Compose:** Orchestrates all services

```
[User] <-> [React Frontend] <-> [FastAPI Backend] <-> [PostgreSQL DB]
                                 |
                                 +--[Gmail SMTP]
```

## Setup and Run Instructions

### Prerequisites
- Docker and Docker Compose installed
- Gmail account and app password for email notifications

### Configuration
1. Edit `docker-compose.yml` and set the following environment variables under the `backend` service:
   - `SMTP_SENDER_EMAIL`: Your Gmail address
   - `SMTP_SENDER_PASSWORD`: Your Gmail app password
   - `NOTIFY_EMAIL`: Recipient email address for notifications

2. (Optional) Update frontend/backend/database settings as needed.

### Build and Start the Application

```bash
docker compose down && docker compose up --build
```

- The frontend will be available at `http://localhost:3000`
- The backend API will be available at `http://localhost:8000`

### Usage
- View pipeline metrics and build executions on the dashboard
- On pipeline failure, an email notification will be sent to the configured recipient

### Stopping the Application

```bash
docker compose down
```

---
For more details, see the `docs/` folder for requirement analysis and technical design documents.
