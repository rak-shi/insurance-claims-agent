## 🧾 Sample Execution & Output

### ▶️ Command Executed

```bash
python main.py "sample fnol/manual_review_fnol.txt"
```

📤 Output (JSON)
```
{
  "extractedFields": {
    "policy_number": "PN12345",
    "policyholder_name": "John Doe",
    "effective_dates": "2022-01-01 - 2023-01-01",
    "incident_date": "2023-03-15",
    "incident_time": "14:30",
    "incident_location": "123 Main St",
    "incident_description": "Vehicle collision",
    "claimant": "John Doe",
    "third_parties": "Jane Smith",
    "contact_details": {
      "Phone": "123-456-7890",
      "Email": "johndoe@example.com"
    },
    "asset_type": "Vehicle",
    "asset_id": "VEH12345",
    "estimated_damage": "$10,000",
    "claim_type": "Property Damage",
    "attachments": [
      {
        "File Name": "incident_report.pdf",
        "File Type": "PDF"
      }
    ],
    "initial_estimate": "$5,000"
  },
  "missingFields": [],
  "recommendedRoute": "Standard Claims Queue",
  "reasoning": "Standard processing applicable."
}
```
### ✅ Explanation

- All mandatory FNOL fields were successfully extracted  
- No missing fields detected during validation  
- Claim does not meet fast-track, injury, or investigation criteria  
- Routed to **Standard Claims Queue** using deterministic rules


## 🧾 Sample Execution & Output – Fast-Track Claim

### ▶️ Command Executed

```bash
python main.py "sample fnol/fasttrack_fnol.txt"
```
📤 Output (JSON)
```
{
  "extractedFields": {
    "policy_number": "AUTO12345",
    "policyholder_name": "John Doe",
    "effective_dates": "01/01/2024 - 01/01/2025",
    "incident_date": "08/12/2024",
    "incident_time": "10:30 AM",
    "incident_location": "Bangalore, KA",
    "incident_description": "Rear-end collision at traffic signal during slow traffic.",
    "claimant": "John Doe",
    "third_parties": "None",
    "contact_details": "9876543210",
    "asset_type": "Automobile",
    "asset_id": "1HGCM82633A123456",
    "estimated_damage": "15000",
    "claim_type": "automobile",
    "attachments": "accident_photos.pdf",
    "initial_estimate": "15000"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage below 25,000."
}
```

### Explanation
- All mandatory FNOL fields were successfully extracted

- No missing or inconsistent fields detected

- Estimated damage is below ₹25,000

- Claim automatically routed to Fast-track using deterministic rules
