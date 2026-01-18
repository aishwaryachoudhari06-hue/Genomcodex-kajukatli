# backend/services/dna_service.py

"""
DNA-related business logic for GenomCodex.
Stores DNA off-chain and anchors hashes on a blockchain ledger.
"""

from uuid import uuid4
from datetime import datetime

from models.dna import DNARecord
from services.fake_db import (
    add_dna_record,
    log_action,
    get_all_dna_records
)

from blockchain.hashing import hash_dna
from blockchain.ledger import create_block


# -----------------------------
# Add DNA Record
# -----------------------------
def add_dna(record: DNARecord, actor: str):
    record_id = str(uuid4())
    dna_hash = hash_dna(record.dna_sequence)

    dna_data = {
        "record_id": record_id,
        "dna_sequence": record.dna_sequence,  # off-chain
        "dna_hash": dna_hash,
        "owner": record.owner,
        "access_level": record.access_level,
        "created_at": datetime.utcnow().isoformat()
    }

    add_dna_record(dna_data)

    block = create_block({
        "action": "ADD_DNA",
        "dna_hash": dna_hash,
        "performed_by": actor
    })

    log_action({
        "action": "ADD_DNA",
        "dna_hash": dna_hash,
        "performed_by": actor,
        "block_hash": block["hash"],
        "timestamp": datetime.utcnow().isoformat()
    })

    return dna_data


# -----------------------------
# Get All DNA Records
# -----------------------------
def get_all_dna():
    return get_all_dna_records()


# -----------------------------
# 🔍 Search DNA by SEQUENCE
# -----------------------------
def search_dna_by_sequence(dna_sequence: str):
    dna_hash = hash_dna(dna_sequence)
    records = get_all_dna_records()

    for record in records:
        if record["dna_hash"] == dna_hash:
            return record

    return None
