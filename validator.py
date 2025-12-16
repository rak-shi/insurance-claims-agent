MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "incident_location",
    "incident_description",
    "estimated_damage",
    "claim_type",
    "attachments",
    "initial_estimate"
]

def find_missing_fields(fields: dict) -> list:
    return [f for f in MANDATORY_FIELDS if not fields.get(f)]
