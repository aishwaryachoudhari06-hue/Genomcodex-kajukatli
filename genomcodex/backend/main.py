# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ---------------------------------
# App Initialization
# ---------------------------------
app = FastAPI(
    title="GenomCodex API",
    description="Secure genomic data platform (MVP)",
    version="0.1.0"
)

# ---------------------------------
# CORS Configuration
# ---------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------
# Health Check Route
# ---------------------------------
@app.get("/")
def health_check():
    return {
        "status": "OK",
        "project": "GenomCodex",
        "message": "Backend is running 🧬"
    }

# ---------------------------------
# Register Routes
# ---------------------------------
from routes import auth, dna, audit, blockchain

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(dna.router, prefix="/dna", tags=["DNA"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])
app.include_router(blockchain.router, prefix="/blockchain", tags=["Blockchain"])
