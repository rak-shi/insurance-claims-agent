##  Sample Execution & Output 
## Standard Claims Queue (Manual Review FNOL)

###  Command Executed

```bash
python main.py "sample fnol/manual_review_fnol.txt"
```

Output (JSON)
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
### Explanation

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
  

## 🧾 Sample Execution & Output – Injury Claim

### ▶️ Command Executed

```bash
python main.py "sample fnol/injury_fnol.txt"
```
📤 Output (JSON)
```
{
  "extractedFields": {
    "policy_number": "AUTO67890",
    "policyholder_name": "Priya Sharma",
    "effective_dates": "05/01/2024 - 05/01/2025",
    "incident_date": "09/01/2024",
    "incident_time": "7:45 PM",
    "incident_location": "Hyderabad, TS",
    "incident_description": "Vehicle skidded on wet road causing minor collision. Driver sustained injuries.",
    "claimant": "Priya Sharma",
    "third_parties": "None",
    "contact_details": "9123456780",
    "asset_type": "Automobile",
    "asset_id": "MA3EUA12S00765432",
    "estimated_damage": "40000",
    "claim_type": "injury",
    "attachments": "medical_report.pdf",
    "initial_estimate": "40000"
  },
  "missingFields": [],
  "recommendedRoute": "Specialist Queue",
  "reasoning": "Injury-related claim."
}
```
### Explanation
- All mandatory FNOL fields were successfully extracted
- No missing fields detected during validation
- Claim type identified as injury
- Automatically routed to Specialist Queue based on deterministic rules

## 🧾 Sample Execution & Output – Investigation Flag (Fraud Indicators)

### ▶️ Command Executed

```bash
python main.py "sample fnol/investigation_fnol.txt"
```
 Output (JSON)
 ```
{
  "extractedFields": {
    "policy_number": "AUTO99999",
    "policyholder_name": "Rahul Verma",
    "effective_dates": "03/01/2024 - 03/01/2025",
    "incident_date": "07/20/2024",
    "incident_time": "11:15 PM",
    "incident_location": "Delhi",
    "incident_description": "Accident circumstances appear inconsistent and possibly staged. Damage pattern does not match description.",
    "claimant": "Rahul Verma",
    "third_parties": "Unknown vehicle",
    "contact_details": "9988776655",
    "asset_type": "Automobile",
    "asset_id": "DL8CAF12345678901",
    "estimated_damage": "60000",
    "claim_type": "automobile",
    "attachments": "claim_form.pdf",
    "initial_estimate": "60000"
  },
  "missingFields": [],
  "recommendedRoute": "Investigation Flag",
  "reasoning": "Potential fraud indicators detected."
}
```
###  Explanation
- All mandatory FNOL fields were successfully extracted
- No missing fields detected during validation
- Incident description contains fraud-related keywords (e.g., inconsistent, staged)
- Claim automatically routed to Investigation Flag for further review using deterministic rules

## 🧾 Sample Execution & Output – Manual Review (Blank / ACORD PDF)

### Command Executed

```bash
python main.py "sample fnol/ACORD-Automobile-Loss-Notice-12.05.16.pdf"
```
Output (JSON)
```
{
  "extractedFields": {
    "policy_number": "POLICY NUMBER",
    "policyholder_name": "INSURED NAME OF INSURED (First, Middle, Last)",
    "effective_dates": null,
    "incident_date": null,
    "incident_time": null,
    "incident_location": "LOCATION OF LOSS",
    "incident_description": "DESCRIPTION OF ACCIDENT",
    "claimant": "INSURED NAME OF INSURED (First, Middle, Last)",
    "third_parties": null,
    "contact_details": {
      "Name": "CONTACT NAME OF CONTACT (First, Middle, Last)",
      "Phone": "CONTACT PHONE #",
      "Email": "PRIMARY E-MAIL ADDRESS"
    },
    "asset_type": "VEHICLE",
    "asset_id": "VEH #",
    "estimated_damage": "ESTIMATE AMOUNT",
    "claim_type": null,
    "attachments": null,
    "initial_estimate": null
  },
  "missingFields": [
    "incident_date",
    "claim_type",
    "attachments",
    "initial_estimate"
  ],
  "recommendedRoute": "Manual Review",
  "reasoning": "Mandatory FNOL fields are missing."
}
```
### Explanation
- Document is a blank / template-style ACORD PDF
- Several mandatory FNOL fields are missing or unfilled
- Validation agent correctly detected missing fields
- Claim routed to Manual Review to prevent unsafe automation
- Demonstrates safe handling of incomplete FNOLs
