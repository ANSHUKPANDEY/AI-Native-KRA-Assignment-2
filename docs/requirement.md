
# CI/CD Pipeline Health Dashboard Application

## Requirement

- Need to create a 3 tier application having front-end, back-end and database end. 
- The application should be able to monitor executions from CI/CD tools like GitHub Actions or Jenkins and should be able to present the results in a Health Dashboard. 
- The application should have a simple front-end UI Dashboard to visualise pipeline metrics and display logs/status of latest builds.
- The application should be able to send alerts (via Slack or Email) on pipeline failures.
- The application should be containerized or running as docker containers.


## The application should be based upon below mentioned technology stack 
- **Backend**: FastAPI (Python)
- **Frontend**: React.js
- **Database**: PostgreSQL

## Features of CI/CD Dashboard UI created by application
- It should be able to collect data on pipeline executions (success/failure, build time, status). 
- It should be able to show real-time metrics like Success/Failure rate, Average build time and last build status
- Dashboard to visualize metrics and list executions.