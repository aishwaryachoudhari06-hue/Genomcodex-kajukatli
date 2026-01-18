# backend/services/fake_db.py

"""
Temporary in-memory database for MVP.
Replaced later with MongoDB.
"""

# -----------------------------
# In-memory stores
# -----------------------------
USERS = []
DNA_RECORDS = []
AUDIT_LOGS = []


# -----------------------------
# USER FUNCTIONS (Auth)
# -----------------------------
def add_user(user: dict):
    if any(u["username"] == user["username"] for u in USERS):
        raise ValueError("User already exists")
    USERS.append(user)
    return user


def get_user_by_username(username: str):
    for user in USERS:
        if user["username"] == username:
            return user
    return None


# -----------------------------
# DNA FUNCTIONS
# -----------------------------
def add_dna_record(dna: dict):
    DNA_RECORDS.append(dna)
    return dna


def get_all_dna_records():
    return DNA_RECORDS


def search_dna(owner=None, dna_hash=None):
    results = DNA_RECORDS

    if owner:
        results = [d for d in results if d["owner"] == owner]

    if dna_hash:
        results = [d for d in results if d["dna_hash"] == dna_hash]

    return results


# -----------------------------
# AUDIT FUNCTIONS
# -----------------------------
def log_action(action: dict):
    AUDIT_LOGS.append(action)
    return action


def get_audit_logs():
    return AUDIT_LOGS
