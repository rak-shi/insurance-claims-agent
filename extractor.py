import pdfplumber
from llm_extractor import llm_extract

def extract_text(path: str) -> str:
    if path.lower().endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_fields(path: str) -> dict:
    text = extract_text(path)
    data = llm_extract(text)

    return {
        "policy_number": data.get("Policy Number"),
        "policyholder_name": data.get("Policyholder Name"),
        "effective_dates": data.get("Effective Dates"),

        "incident_date": data.get("Incident Date"),
        "incident_time": data.get("Incident Time"),
        "incident_location": data.get("Incident Location"),
        "incident_description": data.get("Incident Description"),

        "claimant": data.get("Claimant"),
        "third_parties": data.get("Third Parties"),
        "contact_details": data.get("Contact Details"),

        "asset_type": data.get("Asset Type"),
        "asset_id": data.get("Asset ID"),
        "estimated_damage": data.get("Estimated Damage"),

        "claim_type": data.get("Claim Type"),
        "attachments": data.get("Attachments"),
        "initial_estimate": data.get("Initial Estimate"),
    }
