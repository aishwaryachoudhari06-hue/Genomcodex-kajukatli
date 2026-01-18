# backend/routes/dna.py

from fastapi import APIRouter, HTTPException, Query, status
from models.dna import DNARecord
from services.dna_service import (
    add_dna,
    get_all_dna,
    search_dna_by_sequence
)

router = APIRouter()


# -----------------------------
# Add DNA Record
# -----------------------------
@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_dna_record(
    record: DNARecord,
    actor: str = Query(..., description="Username performing the action")
):
    return {
        "message": "DNA record added successfully",
        "dna": add_dna(record, actor)
    }


# -----------------------------
# Get All DNA Records
# -----------------------------
@router.get("/all")
def fetch_all_dna():
    return get_all_dna()


# -----------------------------
# 🔍 Search DNA (BY SEQUENCE)
# -----------------------------
@router.post("/search")
def search_dna(sequence: str = Query(..., description="DNA sequence to search")):
    result = search_dna_by_sequence(sequence)

    if not result:
        raise HTTPException(status_code=404, detail="DNA record not found")

    return result
