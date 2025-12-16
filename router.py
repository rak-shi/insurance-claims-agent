KEYWORDS = ["fraud", "staged", "inconsistent"]

def route_claim(fields: dict, missing_fields: list) -> tuple:
    if missing_fields:
        return "Manual Review", "Mandatory FNOL fields are missing."

    if any(k in fields["incident_description"].lower() for k in KEYWORDS):
        return "Investigation Flag", "Potential fraud indicators detected."

    if fields["claim_type"].lower() == "injury":
        return "Specialist Queue", "Injury-related claim."

    try:
        if int(fields["estimated_damage"]) < 25000:
            return "Fast-track", "Estimated damage below 25,000."
    except:
        pass

    return "Standard Claims Queue", "Standard processing applicable."
