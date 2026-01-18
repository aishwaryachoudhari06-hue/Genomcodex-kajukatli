# backend/routes/audit.py

from fastapi import APIRouter
from services.fake_db import get_audit_logs

router = APIRouter()

# -----------------------------
# Get Audit Logs
# -----------------------------
@router.get("/all")
def fetch_audit_logs():
    """
    Returns all audit log entries.
    (Access control will be added later)
    """
    return get_audit_logs()
