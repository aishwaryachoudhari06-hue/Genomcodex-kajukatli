# backend/blockchain/ledger.py

from datetime import datetime
import hashlib

BLOCKCHAIN = []

def create_block(data: dict) -> dict:
    previous_hash = BLOCKCHAIN[-1]["hash"] if BLOCKCHAIN else "GENESIS"

    block_content = {
        "index": len(BLOCKCHAIN),
        "timestamp": datetime.utcnow().isoformat(),
        "data": data,
        "previous_hash": previous_hash
    }

    block_hash = hashlib.sha256(
        str(block_content).encode()
    ).hexdigest()

    block = {
        **block_content,
        "hash": block_hash
    }

    BLOCKCHAIN.append(block)
    return block

def get_chain():
    return BLOCKCHAIN
