import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPT = """
You are an insurance FNOL extraction agent.

Extract the following fields from the FNOL document.
If a field is missing, return null.

Return STRICT JSON only.
Do NOT include explanations, markdown, or text outside JSON.

Required JSON keys (exactly these names):

Policy Number
Policyholder Name
Effective Dates
Incident Date
Incident Time
Incident Location
Incident Description
Claimant
Third Parties
Contact Details
Asset Type
Asset ID
Estimated Damage
Claim Type
Attachments
Initial Estimate
"""

def extract_json(text: str) -> dict:
    """
    Safely extract JSON object from LLM response.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in LLM response")
    return json.loads(match.group())

def llm_extract(text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": text[:6000]}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content

    # 🔍 Uncomment this ONCE if you want to see raw output
    # print("RAW LLM OUTPUT:\n", raw)

    try:
        return extract_json(raw)
    except Exception as e:
        print("⚠️ LLM JSON parsing failed:", e)
        return {}
