from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import builds, metrics, webhooks, ws

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(builds.router)
app.include_router(metrics.router)
app.include_router(webhooks.router)
app.include_router(ws.router)

@app.get("/")
def read_root():
    return {"message": "CI/CD Health Dashboard Backend is running"}
