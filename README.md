# 🧬 GenomCodex — Blockchain-Backed Genomic Data Prototype

GenomCodex is a privacy-first genomic data management prototype that demonstrates how blockchain can be used responsibly to ensure the integrity, traceability, and auditability of sensitive DNA records without storing raw genomic data on-chain.

This project was built as a hackathon MVP to showcase correct system architecture and blockchain usage, not full-scale production deployment.

🚀 Key Features

🔐 Off-chain DNA storage (privacy preserved)

⛓️ Blockchain-anchored DNA hash records

🧾 Immutable audit trail linked to blockchain blocks

🧬 DNA verification using cryptographic hashing

👥 Role-based frontend access

Medical / Admin → Add & Search DNA

Forensic → Read-only DNA verification

🖥️ Professional multi-page frontend UI

⚡ FastAPI backend

🧠 Architecture Overview
Data Flow

DNA Input
→ SHA-256 Hash
→ Off-chain DNA Storage
→ Blockchain Ledger (Hash only)
→ Audit Log (Linked to Block)

Blockchain Design

Raw DNA is NOT stored on blockchain

Only cryptographic hashes are stored

Ensures:

Privacy

Immutability

Tamper detection

Auditability

This follows a hybrid blockchain architecture, commonly used in real-world systems.

🏗️ Tech Stack
Backend

Python

FastAPI

In-memory storage (MVP)

SHA-256 hashing

Custom blockchain ledger

Frontend

HTML

CSS (base + polish layer)

Vanilla JavaScript

Role-based UI routing

📁 Project Structure

genomcodex/
├── backend/
│ ├── main.py
│ ├── routes/
│ │ ├── dna.py
│ │ ├── audit.py
│ │ └── blockchain.py
│ ├── services/
│ │ ├── dna_service.py
│ │ └── fake_db.py
│ ├── blockchain/
│ │ ├── hashing.py
│ │ └── ledger.py
│ └── models/
│ └── dna.py
│
└── frontend/
├── index.html (Login)
├── dashboard.html (Medical / Admin)
├── dna.html (DNA Records)
├── audit.html (Audit Trail)
├── blockchain.html (Blockchain Ledger)
├── forensic.html (Forensic Verification)
├── css/
│ ├── style.css
│ └── polish.css
└── README.md

▶️ How to Run the Prototype
Start Backend

cd backend
python -m uvicorn main:app --reload

Backend URL:
http://127.0.0.1:8000

API Docs:
http://127.0.0.1:8000/docs

Start Frontend

cd frontend
python -m http.server 5500

Open in browser:
http://127.0.0.1:5500/index.html

👤 User Roles (Frontend-Enforced for MVP)

Role | Capabilities
Medical | Add DNA, Search DNA, View Audit, View Blockchain
Admin | Same as Medical (UI variation)
Forensic | Search & Verify DNA only (Read-only)

Authentication and RBAC are simulated on the frontend for MVP speed.

🔍 DNA Verification Logic

User inputs DNA sequence

System hashes DNA using SHA-256

Hash is matched against blockchain ledger

If found → DNA integrity is verified

Raw DNA is never exposed during verification.

⚠️ MVP Limitations (Intentional)

In-memory storage (no MongoDB)

Simulated authentication

Local blockchain ledger

No real Ethereum integration

These limitations are intentional due to hackathon time constraints.

🌱 Future Improvements

MongoDB integration

JWT-based authentication

Backend role-based access control

Ethereum / Hyperledger deployment

Encrypted DNA storage

Smart contract anchoring

🏆 Why This Approach Is Correct

Blockchain used only where immutability is required

Sensitive genomic data remains private

Verifiable integrity without data exposure

Architecture scales to real production systems

📢 Final Note

GenomCodex is a working hybrid blockchain prototype, not a mockup.
It demonstrates responsible blockchain usage for genomic data security.
