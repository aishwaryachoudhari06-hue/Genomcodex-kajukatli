# backend/blockchain/hashing.py

import hashlib

def hash_dna(sequence: str) -> str:
    """
    Generates SHA-256 hash of DNA sequence.
    This hash is what goes 'on-chain'.
    """
    return hashlib.sha256(sequence.encode()).hexdigest()
