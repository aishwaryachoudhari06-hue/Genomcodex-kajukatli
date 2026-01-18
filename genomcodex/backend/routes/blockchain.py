# backend/routes/blockchain.py

from fastapi import APIRouter
from blockchain.ledger import get_chain

router = APIRouter()

@router.get("/all")
def get_blockchain():
    """
    Returns the entire blockchain ledger.
    """
    return get_chain()
