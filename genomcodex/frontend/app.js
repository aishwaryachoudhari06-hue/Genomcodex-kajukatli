const API = "http://127.0.0.1:8000";

// --------------------
// ADD DNA
// --------------------
async function submitDNA() {
  const dna = document.getElementById("dnaSequence").value;
  const owner = document.getElementById("owner").value;
  const access = document.getElementById("accessLevel").value;

  const res = await fetch(`${API}/dna/add?actor=${owner}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      dna_sequence: dna,
      owner: owner,
      access_level: access
    })
  });

  const data = await res.json();
  document.getElementById("dnaResult").textContent =
    JSON.stringify(data, null, 2);
}

// --------------------
// SEARCH DNA
// --------------------
async function searchDNA() {
  const owner = document.getElementById("searchOwner").value;
  const hash = document.getElementById("searchHash").value;

  let url = `${API}/dna/search?`;
  if (owner) url += `owner=${owner}&`;
  if (hash) url += `dna_hash=${hash}`;

  const res = await fetch(url);
  const data = await res.json();

  document.getElementById("searchResult").textContent =
    JSON.stringify(data, null, 2);
}

// --------------------
// AUDIT LOGS
// --------------------
async function loadAudit() {
  const res = await fetch(`${API}/audit/all`);
  const data = await res.json();

  document.getElementById("auditLogs").textContent =
    JSON.stringify(data, null, 2);
}

// --------------------
// BLOCKCHAIN
// --------------------
async function loadBlockchain() {
  const res = await fetch(`${API}/blockchain/all`);
  const data = await res.json();

  document.getElementById("blockchainData").textContent =
    JSON.stringify(data, null, 2);
}
