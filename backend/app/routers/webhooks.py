from fastapi import APIRouter

router = APIRouter(prefix="/webhooks", tags=["webhooks"])

@router.post("/github")
def github_webhook(payload: dict):
    # Process GitHub Actions webhook payload
    return {"status": "received", "source": "github", "payload": payload}

@router.post("/jenkins")
def jenkins_webhook(payload: dict):
    # Process Jenkins webhook payload
    return {"status": "received", "source": "jenkins", "payload": payload}
